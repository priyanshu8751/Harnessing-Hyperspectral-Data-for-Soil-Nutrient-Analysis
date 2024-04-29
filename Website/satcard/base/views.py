import json
from collections import Counter
from datetime import timedelta, datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.db.models import Count, Max, Min, F, Window, ExpressionWrapper, DateTimeField
from django.db.models.functions import Lag

from base.models import RawPayload, Device, Data, ParamGroup, ParamConfig


def send_response(message, success=True):
	to_json = {
		"success": success,
		"message": message
	}
	return HttpResponse(json.dumps(to_json), content_type="Application/json")

def replace_none_to_empty_str(list_of_objs):
	new_list_of_objs = []
	for obj in list_of_objs:
		new_list_of_objs.append({key: val if val != None else '' for key, val in obj.items()})
	return new_list_of_objs


def rawdata(request):
	"""This is GET API to receive the raw data and store into raw payload table."""
	api_key = request.GET.get('api_key', None)
	if not api_key:
		return send_response("API KEY is required!", success=False)
	payload = request.META['QUERY_STRING']
	timestamp = datetime.now()
	try:
	    raw_payload = RawPayload(timestamp=timestamp, payload=payload).save()
	except Exception as err:
		print(str(err))
		return send_response("Something went wrong!", success=False)
	return send_response("Data saved!")


def get_data_availability(start_time, end_time, device_id_list=None):
	if device_id_list is None:
		device_id_list = list(Device.objects.values_list('id', flat=True))
	data_count = list(Data.objects.filter(
		timestamp__gte=start_time, timestamp__lte=end_time, device_id__in=device_id_list
	).values('device').annotate(count=Count('device')))
	data_count = {obj['device']: obj['count'] for obj in data_count}
	return data_count


def last_heard_at(time_to_check=None, device_id_list=None):
	if time_to_check == None:
		time_to_check = datetime.now()
	if device_id_list is None:
		device_id_list = list(Device.objects.values_list('id', flat=True))
	latest_data = list(Data.objects.filter(
		timestamp__lte=time_to_check, device_id__in=device_id_list
	).values('device').annotate(last_heard=Max('timestamp')))
	last_heard_map = {obj['device']: [str(obj['last_heard']), (time_to_check - obj['last_heard'].replace(tzinfo=None)).total_seconds() / 3600.0] for obj in latest_data}
	return last_heard_map


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
	template_name = 'dashboard/index.html'

	def get_context_data(self, *args, **kwargs):
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		devices = list(Device.objects.values(
			'id', 'name', 'address', 'city', 'state', 'version', 'latitude', 'longitude'))
		devices = replace_none_to_empty_str(devices)
		end_time = datetime.now()
		start_time = end_time.replace(hour=0, minute=0, second=0)
		data_availability = get_data_availability(start_time, end_time)
		time_diff = (end_time - start_time).total_seconds() / 60.0
		expected_datapoints = time_diff // 10  # expecting one data point per 10 minutes per device

		last_heard_map = last_heard_at(end_time)

		context['devices'] = devices
		data_count = Data.objects.count()
		context['data_count'] = data_count
		context['data_availability'] = data_availability
		context['expected_datapoints'] = expected_datapoints
		context['last_heard_map'] = last_heard_map
		return context


@method_decorator(login_required, name='dispatch')
class DeviceView(TemplateView):
    template_name = 'dashboard/device.html'

    def get_context_data(self, *args, **kwargs):
        device_id = kwargs.get('device_id', None)
        context = super(DeviceView, self).get_context_data(*args, **kwargs)
        devices = Device.objects.all()
        dev_obj = devices.filter(id=device_id)
        if dev_obj.exists():
        	dev_obj = dev_obj[0]
        context['device'] = dev_obj
        context['devices'] = devices.values('id', 'name')

        param_group = list(ParamGroup.objects.values())
        context['param_group'] = param_group

        return context
    
from django.db.models import Count



@method_decorator(login_required, name='dispatch')
class DeviceSatelliteView(TemplateView):
	template_name = 'satellite/satellite.html'

@method_decorator(login_required, name='dispatch')
class DeviceReportView(TemplateView):
    template_name = 'reports/device-report.html'
    def get_context_data(self, *args, **kwargs):
        device_id = kwargs.get('device_id', 1)
        context = super(DeviceReportView, self).get_context_data(*args, **kwargs)
        devices = Device.objects.all()
        dev_obj = devices.filter(id=device_id)
        if dev_obj.exists():
            dev_obj = dev_obj[0]
        context['device'] = dev_obj
        context['devices'] = devices.values('id', 'name')
        param_group = list(ParamGroup.objects.values())
        context['param_group'] = param_group
        return context

def get_data_report(request):
	device_id = request.GET.get('device_id')
	date_gte = request.GET.get('date_gte')
	date_lte = request.GET.get('date_lte')

	start_time = datetime.strptime(date_gte, "%Y-%m-%d")
	end_time = datetime.strptime(date_lte, "%Y-%m-%d")
	end_time = end_time.replace(hour=23, minute=59, second=59)

	queryset = Data.objects.filter(device_id=device_id, timestamp__gte=start_time, timestamp__lte=end_time).order_by('timestamp')
	exclude_fields = ['id', 'device', 'timestamp']
	field_list = [field.name for field in Data._meta.get_fields() if field.name not in exclude_fields]
	min_max_values = queryset.aggregate(*[Min(field) for field in field_list], *[Max(field) for field in field_list])
	min_values = {key[:-5]:val for key, val in min_max_values.items() if key.endswith("__min")}  # [:-5] to remove __min at end
	max_values = {key[:-5]:val for key, val in min_max_values.items() if key.endswith("__max")}

	annotations = {}
	for field in field_list:
	    annotations[f'lagged_{field}'] = Window(expression=Lag(field))
	    annotations[f'delta_{field}'] = F(field) - F(f'lagged_{field}')

	max_deltas = queryset.annotate(**annotations).aggregate(
	    **{field: Max(f'delta_{field}') for field in field_list}
	)

	param_config = ParamConfig.objects.all()
	param_config = {obj.param: obj for obj in param_config}

	param_wise_data = []
	for param in field_list:
		exp_min, exp_max, unit, max_expected_delta= '-', '-', '-', '-'
		param_config_obj = param_config.get(param, None)
		if param_config_obj != None:
			exp_min, exp_max, unit, max_expected_delta = param_config_obj.min_limit, \
				param_config_obj.max_limit, param_config_obj.unit, param_config_obj.max_expected_delta
		param_wise_data.append({
			"param": param,
			"min_val": round(min_values[param], 2) if min_values[param] is not None else None,
			"max_val": round(max_values[param], 2) if max_values[param] is not None else None,
			"max_delta": round(max_deltas[param], 2) if max_deltas[param] is not None else None,
			"expected_min": exp_min,
			"expected_max": exp_max,
			"max_expected_delta": max_expected_delta,
			"unit": unit
		})

	data_points = queryset.values_list('timestamp', flat=True)
	intervals = [(second - first).total_seconds() for first, second in zip(data_points, data_points[1:])]
	interval_counts = Counter(intervals)
	try:
		most_common_interval = interval_counts.most_common(1)[0]
		data_time_interval = timedelta(seconds=most_common_interval[0])
		expected_datapoints = (end_time - start_time) / data_time_interval
	except:
		data_time_interval = 0
		expected_datapoints = 0

	received_datapoints = queryset.count()
	try:
		expected_datapoints_percent = (received_datapoints / expected_datapoints) * 100
	except ZeroDivisionError:
		expected_datapoints_percent = 0

	result = {
		"param_wise_data": param_wise_data,
		"total_data_points": received_datapoints,
		"expected_datapoints": round(expected_datapoints, 0),
		"expected_datapoints_percent": round(expected_datapoints_percent, 2),
		"interval": str(data_time_interval)
	}

	return JsonResponse(result, safe=False)


@method_decorator(login_required, name='dispatch')
class FarmerDashboard(TemplateView):
    template_name = 'dashboard/farmer_dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FarmerDashboard, self).get_context_data(*args, **kwargs)
        context['test'] = "test"
        return context


@method_decorator(login_required, name='dispatch')
class CropView(TemplateView):
    template_name = 'dashboard/crop.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CropView, self).get_context_data(*args, **kwargs)
        context['test'] = "test"
        return context

