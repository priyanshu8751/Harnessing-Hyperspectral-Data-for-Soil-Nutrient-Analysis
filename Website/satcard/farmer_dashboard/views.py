from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from datetime import datetime, date, timedelta
from django.http import Http404
from base.models import Device, Data, ParamConfig
from farmer_dashboard.models import Farmer, CropType, Crop, GDDRecord, Alert, Task
from django.db.models import Sum
import json, requests
from django.conf import settings 
from django.utils.timezone import now
class IndexView(View):
    template_name = 'farmer_dashboard/index.html'

    #returns device_id
    def get_device(self, device_id): 
        try:
            return Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            raise Http404("Device does not exist")

   #returns latest data of the device returns device name and  timestamp
    def get_latest_data(self, device_id, today):
        try:
            return Data.objects.filter(device_id=device_id, timestamp__date=today).latest('timestamp')
        except Data.DoesNotExist:
            # If no data for today, get the most recent data
            return Data.objects.filter(device_id=device_id).latest('timestamp')

    # 
    def get_weather_data(self, device_id):
        try:
            
            latest_data = self.get_latest_data(device_id, datetime.now().today())
            
            return {
            'timestamp': latest_data.timestamp.isoformat() if latest_data else None,
            'temperature': latest_data.temperature if latest_data else None,
            'windspeed': latest_data.wind_speed if latest_data else None,
            'irradiance': latest_data.irradiance if latest_data else None,
            'rainfall': latest_data.rainfall if latest_data else None,
            'humidity': latest_data.humidity if latest_data else None,
            'sm1': latest_data.sm1 if latest_data else None,
            'sm2': latest_data.sm2 if latest_data else None,
            'leaf_wetness': latest_data.leaf_wetness if latest_data else None,
                
            }
        except Data.DoesNotExist:
            return {}

    def get_context_data(self, **kwargs):
        device_id = kwargs.get('device_id')
        devices = Device.objects.all()

        dev_obj = self.get_device(device_id)

        # farmers = Farmer.objects.all()
        # crop_types = CropType.objects.all()
        # crops = Crop.objects.filter(farmer=dev_obj)

        context = {
            'device_id': device_id,
            'device_name': dev_obj.name,  # Add more fields as needed

            # 'farmers': farmers,
            # 'crop_types': crop_types,
            # 'crops': crops,
            
        }

        # Get weather data
        weather_data = self.get_weather_data(device_id)
        context.update(weather_data)

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)



def WmsCard(request, device_id):

    def get_device(self, device_id): 
        try:
            return Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            raise Http404("Device does not exist")


    def get_latest_data(device_id, today):
        try:
            return Data.objects.filter(device_id=device_id, timestamp__date=today).latest('timestamp')
        except Data.DoesNotExist:
            # If no data for today, get the most recent data
            return Data.objects.filter(device_id=device_id).latest('timestamp')

    try:
        # Get the device associated with the provided device_id
        device = Device.objects.get(id=device_id)
    except Device.DoesNotExist:
        return JsonResponse({'error': 'Device not found'}, status=404)

    try:
        # Get the crop associated with the device
        crop = Crop.objects.get(device=device)
    except Crop.DoesNotExist:
        return JsonResponse({'error': 'Crop not found'}, status=404)
    
    crop_type = crop.crop_type
    
    today = datetime.now().today()
    last_updated = datetime.now().strftime('%I:%M %p · %b %d, %Y')
    latest_data = get_latest_data(device_id, today)

     # Calculate GDD for the current day
    planting_date = crop.date_of_planting
    daily_gdd = 0  # Default to 0 if no data available
    if latest_data:
        # Determine if the crop is Kharif or Rabi based on the date of plantation
        if 6 <= planting_date.month <= 10:  # June to October
            Tb = 10
        else:  # November to May
            Tb = 5
        
        tmax = min(latest_data.temperature_max, 30 if Tb == 10 else 25)
        avg_temp = (latest_data.temperature_min + tmax) / 2
        daily_gdd = max(avg_temp - Tb, 0)
    

    data = {
        'device_id': device_id,
        'device_name': Device.objects.get(id=device_id).name,
        'timestamp': latest_data.timestamp.isoformat() if latest_data else None,
        'temperature': latest_data.temperature if latest_data else None,
        'windspeed': latest_data.wind_speed if latest_data else None,
        'irradiance': latest_data.irradiance if latest_data else None,
        'rainfall': latest_data.rainfall if latest_data else None,
        'humidity': latest_data.humidity if latest_data else None,
        'sm1': latest_data.sm1 if latest_data else None,
        'sm2': latest_data.sm2 if latest_data else None,
        'leaf_wetness': latest_data.leaf_wetness if latest_data else None,
        'wind_direction': latest_data.wind_direction if latest_data else None,
        'last_updated': last_updated,
        'daily_gdd': daily_gdd,
    }
    if crop_type:
        data['wms_background_url'] = crop_type.wms_background.url  
    

    # json_string = json.dumps(data)
    # return JsonResponse(json_string, safe=False)

    return JsonResponse(data)


class MapCard(View):
    def get(self, request, *args, **kwargs):
        device_id = kwargs.get('device_id')
        boundary_only = request.GET.get('boundary_only') == 'true'  # Check for query parameter

        try:
            # Get the device associated with the provided device_id
            device = Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            return JsonResponse({'error': 'Device not found'}, status=404)

        try:
            # Get the crop associated with the device
            crop = Crop.objects.get(device=device)
        except Crop.DoesNotExist:
            return JsonResponse({'error': 'Crop not found'}, status=404)

        # Now, retrieve the farmer associated with the crop
        farmer = crop.farmer
        today = datetime.now().today()

        last_updated = datetime.now().strftime('%I:%M %p · %b %d, %Y')
        crop_type = crop.crop_type

        try:
            latest_data = Data.objects.filter(device=device).latest('timestamp')
        except Data.DoesNotExist:
            latest_data = None

        # Construct the data based on the request type
        if boundary_only:
            # Return only boundary coordinates
            coordinates = [coordinate.split('|') for coordinate in crop.boundary_coordinates.split('|')]
            return JsonResponse({'boundary_coordinates': coordinates})
        else:
            icon_url = crop_type.icon.url
            wms_background_url = crop_type.wms_background.url
            profile_pic_url=farmer.profile_pic.url
            seed_phase_url = crop_type.seed_phase.url
            seedling_phase_url = crop_type.seedling_phase.url
            vegetative_phase_url =  crop_type.vegetative_phase.url
            flowering_phase_url = crop_type.flowering_phase.url
            ripening_phase_url = crop_type.ripening_phase.url
        
            # Return complete farmer data
            farmer_data = {
                'farmer_id': farmer.id,
                'device_id': device_id,
                'farmers_name': farmer.name,
                'address': farmer.address,
                'crop_type_name': crop_type.name,
                'crop_name': crop.name,
                'boundary_coordinates': crop.boundary_coordinates,
                'area_covered': crop.area_covered,
                'icon_url': icon_url,
                'profile_pic_url':profile_pic_url,
                'last_updated': last_updated,
            }
            return JsonResponse(farmer_data)

class GDDCard(View):
    def get(self, request, *args, **kwargs):
        device_id = kwargs.get('device_id')
        try:
            device = Device.objects.get(id=device_id)
            crop = Crop.objects.get(device=device)
        except (Device.DoesNotExist, Crop.DoesNotExist):
            return JsonResponse({'error': 'Device or Crop not found'}, status=404)

        planting_date = crop.date_of_planting
        today = date.today()
        one_day = timedelta(days=1)
        current_date = planting_date

        while current_date <= today:
            data_for_day = Data.objects.filter(device_id=device_id, timestamp__date=current_date).order_by('-timestamp').first()
            if data_for_day:
                # Determine if the crop is Kharif or Rabi based on the date of plantation
                if 6 <= current_date.month <= 10:  # June to October
                    Tb = 10
                else:  # November to May
                    Tb = 5

                tmax = min(data_for_day.temperature_max, 30 if Tb == 10 else 25)
                avg_temp = (data_for_day.temperature_min + tmax) / 2
                daily_gdd = max(avg_temp - Tb, 0)

                # Store or update daily GDD
                GDDRecord.objects.update_or_create(
                    crop=crop,
                    date=current_date,
                    defaults={'gdd_value': daily_gdd}
                )

            current_date += one_day

        # Calculate cumulative GDD
        cumulative_gdd = GDDRecord.objects.filter(
            crop=crop,
            date__lte=today
        ).aggregate(total_gdd=Sum('gdd_value'))['total_gdd'] or 0
            
        last_updated = datetime.now().strftime('%I:%M %p · %b %d, %Y')
        crop_type = crop.crop_type
        seed_phase_url = crop_type.seed_phase.url
        seedling_phase_url = crop_type.seedling_phase.url
        vegetative_phase_url =  crop_type.vegetative_phase.url
        flowering_phase_url = crop_type.flowering_phase.url
        ripening_phase_url = crop_type.ripening_phase.url


        


        stages_flags = {
            'has_seed_stage': crop_type.has_seed_stage,
            'has_seedling_stage': crop_type.has_seedling_stage,
            'has_vegetative_stage': crop_type.has_vegetative_stage,
            'has_flowering_stage': crop_type.has_flowering_stage,
            'has_ripening_stage': crop_type.has_ripening_stage,
        }

        gdd_limits = [
            crop_type.seed_phase_gdd_limit if crop_type.has_seed_stage else 0,
            crop_type.seedling_phase_gdd_limit if crop_type.has_seedling_stage else 0,
            crop_type.vegetative_phase_gdd_limit if crop_type.has_vegetative_stage else 0,
            crop_type.flowering_phase_gdd_limit if crop_type.has_flowering_stage else 0,
            crop_type.ripening_phase_gdd_limit if crop_type.has_ripening_stage else 0,
        ]
        highest_gdd_limit = max(gdd_limits)
        
        # Ensure highest_gdd_limit is not zero to avoid division by zero error
        if highest_gdd_limit > 0:
            total_growth_value = (cumulative_gdd / highest_gdd_limit) * 100
        else:
            total_growth_value = 0

        # Update the crop's total growth value
        crop.total_growth = total_growth_value
        crop.save()

        return JsonResponse(
            {
            'gdd': daily_gdd,
            'cumulative_gdd': cumulative_gdd,
            'seed_phase_gdd_limit': crop_type.seed_phase_gdd_limit if crop_type.has_seed_stage else 0,
            'seedling_phase_gdd_limit': crop_type.seedling_phase_gdd_limit if crop_type.has_seedling_stage else 0,
            'vegetative_phase_gdd_limit': crop_type.vegetative_phase_gdd_limit if crop_type.has_vegetative_stage else 0,
            'flowering_phase_gdd_limit': crop_type.flowering_phase_gdd_limit if crop_type.has_flowering_stage else 0,
            'ripening_phase_gdd_limit': crop_type.ripening_phase_gdd_limit if crop_type.has_ripening_stage else 0,
            'seed_phase':seed_phase_url,
            'seedling_phase':seedling_phase_url,
            'vegetative_phase':vegetative_phase_url,
            'flowering_phase':flowering_phase_url,
            'ripening_phase':ripening_phase_url,
            'date_of_plantation': crop.date_of_planting, 
            'total_growth_value': total_growth_value,
            'yield_predicted_value':crop.Yield_predicted,
            'last_updated': last_updated,
            'planting_date': planting_date,
            'stages_flags': stages_flags
            }
            )
    

def get_weather_forecast(request, *args, **kwargs):
    device_id = kwargs.get('device_id')
    api_key = settings.WEATHER_API_KEY
    # location = request.GET.get('location', 'Palakkad')  # Default to Paris if no location is provided
    # days = 7  # For a 7-day forecast, including today
    base_url = "http://api.weatherapi.com/v1/forecast.json"


    try:
        # Get the device associated with the provided device_id
        device = Device.objects.get(id=device_id)
    except Device.DoesNotExist:
        return JsonResponse({'error': 'Device not found'}, status=404)



    try:
        # Get the crop associated with the device
        crop = Crop.objects.get(device=device)
    except Crop.DoesNotExist:
        return JsonResponse({'error': 'Crop not found'}, status=404)


    try:
        
        # Extracting the first set of coordinates
        first_coords = crop.boundary_coordinates.split('|')[0]
        latitude, longitude = first_coords.split(', ')
        params = {
            "key": api_key,
            "q": f"{latitude},{longitude}",
            "days": 7,  # For a 7-day forecast
            "aqi": "no",
            "alerts": "no"
        }





        response = requests.get(base_url, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        forecast_data = response.json()
        
        if forecast_data:
            location = forecast_data["location"]
            summary = {
                "location": {
                    "name": location["name"],
                    "region": location["region"],
                    "country": location["country"],
                    "latitude": location["lat"],
                    "longitude": location["lon"],
                    "localtime": location["localtime"],
                },
                "today": {
                    "Average Temperature": forecast_data["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
                    "Total Precipitation": forecast_data["forecast"]["forecastday"][0]["day"]["totalprecip_mm"],
                    "Average Humidity": forecast_data["forecast"]["forecastday"][0]["day"]["avghumidity"],
                    "Wind Speed (kph)": forecast_data["forecast"]["forecastday"][0]["day"]["maxwind_kph"],
                    "Condition": forecast_data["forecast"]["forecastday"][0]["day"]["condition"]["text"],  # Weather condition text
                    "Icon": "http:" + forecast_data["forecast"]["forecastday"][0]["day"]["condition"]["icon"], 
                },
                "tomorrow": {
                    "Average Temperature": forecast_data["forecast"]["forecastday"][1]["day"]["avgtemp_c"],
                    "Total Precipitation": forecast_data["forecast"]["forecastday"][1]["day"]["totalprecip_mm"],
                    "Average Humidity": forecast_data["forecast"]["forecastday"][1]["day"]["avghumidity"],
                    "Wind Speed (kph)": forecast_data["forecast"]["forecastday"][1]["day"]["maxwind_kph"],
                    # "Condition": forecast_data["forecast"]["forecastday"][1]["day"]["condition"]["text"],  # Weather condition text
                    # "Icon": "http:" + forecast_data["forecast"]["forecastday"][1]["day"]["condition"]["icon"],
                },
                "next_week_summary": [
                    {
                        "Date": day["date"],
                        "Avg Temp": day["day"]["avgtemp_c"],
                        "Precipitation": day["day"]["totalprecip_mm"],
                        "Humidity": day["day"]["avghumidity"],
                        "Wind Speed (kph)": day["day"]["maxwind_kph"],  # Assuming total precipitation as rainfall
                        # "Condition": day["day"]["condition"]["text"],  # Weather condition text
                         "Icon": "http:" + day["day"]["condition"]["icon"],
                    } 
                    for day in forecast_data["forecast"]["forecastday"]
                ]
            }
            return JsonResponse(summary)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def get_param_config(request):
    # Retrieve the 'param' from the query parameters
    param_name = request.GET.get('param', None)
    
    # Find the ParamConfig for the given parameter
    if param_name:
        try:
            param_config = ParamConfig.objects.get(param=param_name)
            data = {
                'param': param_config.param,
                'unit': param_config.unit,
                'min_limit': param_config.min_limit,
                'max_limit': param_config.max_limit,
                'max_expected_delta': param_config.max_expected_delta
            }
            return JsonResponse(data)
        except ParamConfig.DoesNotExist:
            return JsonResponse({'error': 'Parameter configuration not found'}, status=404)
    else:
        return JsonResponse({'error': 'Parameter name not specified'}, status=400)
    
class AlertNotifications(View):
    def get(self, request, device_id):
        try:
            device = Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            return JsonResponse({'error': 'Device not found'}, status=404)

        crops = Crop.objects.filter(device=device)

        if not crops.exists():
            return JsonResponse({'error': 'No crops found for the given device.'}, status=404)

        alerts_list = []
        for crop in crops:
            alerts = Alert.objects.filter(crop=crop).values(
                'id', 'alert_type', 'description', 'datetime'
            )
            for alert in alerts:
                # Formatting the datetime to include both date and time
                alert['datetime'] = alert['datetime'].strftime("%Y-%m-%d %H:%M:%S") if alert['datetime'] else None
                alerts_list.append(alert)

        return JsonResponse(alerts_list, safe=False)

    
class FarmerDevicesView(View):
    def get(self, request, device_id):
        try:
            # Get the device with the provided device_id
            device = Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            return JsonResponse({'error': 'Device not found'}, status=404)

        # Get the crop associated with the device
        try:
            crop = Crop.objects.get(device=device)
        except Crop.DoesNotExist:
            return JsonResponse({'error': 'Crop not found for the given device.'}, status=404)

        # Get the farmer associated with the crop
        farmer = crop.farmer

        # Now get all devices associated with crops that belong to this farmer
        crops = Crop.objects.filter(farmer=farmer)
        devices = Device.objects.filter(crop__in=crops).distinct()

        # Create a list of devices with their names and coordinates to return
        devices_list = [
            {
                'id': dev.id,
                'name': dev.name,
                'latitude': dev.latitude,
                'longitude': dev.longitude
            } for dev in devices
        ]

        return JsonResponse(devices_list, safe=False)


class TasksCardView(View):
    def get(self, request, device_id):
        try:
            # Get the device with the provided device_id
            device = Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            return JsonResponse({'error': 'Device not found'}, status=404)

        try:
            crop = Crop.objects.get(device=device)
        except Crop.DoesNotExist:
            return JsonResponse({'error': 'Crop not found for the given device.'}, status=404)

        today = now().date()


       
        # Get upcoming tasks
        upcoming_tasks = crop.tasks.filter(is_completed=False, deadline__gte=today).order_by('deadline')
        upcoming_tasks_data = [
            {
                'task_description': task.description,
                'days_left': (task.deadline - today).days,
            }
            for task in upcoming_tasks
        ]

       # Get all completed tasks
        completed_tasks = crop.tasks.filter(is_completed=True).order_by('-completed_date')
        completed_tasks_data = [
            {
                'task_description': task.description,
                'completed_on': task.completed_date.isoformat() if task.completed_date else None,
            }
            for task in completed_tasks
        ]

        return JsonResponse({
            'upcoming_tasks': upcoming_tasks_data,
            'completed_tasks': completed_tasks_data,
        })

