import datetime as dt

from django.apps import AppConfig
from django.db.models.signals import post_save


fields_map = {
    "api_key": "",
    "Epoch": "",
    "Tmin": "temperature_min",
    "Tmax": "temperature_max",
    "Temp": "temperature",
    "Pressure": "pressure",
    "Humidity": "humidity",
    "Irradiance": "irradiance",
    "WindSpeed": "wind_speed",
    "WindDirection": "wind_direction",
    "Rainfall": "rainfall",
    "InternalTemp": "internal_temperature",
    "DP_avg": "dp_avg",
    "Reset": "reset_count",
    "SM1": "sm1",
    "SM2": "sm2",
    "LeafWetness": "leaf_wetness",
    "BatteryVolt": "battery_volt"

}
accepted_fields = fields_map.keys()


def save_to_data(rawdata):
    from base.models import Device, Data

    timestamp = rawdata.timestamp
    payload = rawdata.payload
    tags = payload.split('&')
    devices_data = {}
    device_obj = None
    data = {}
    for tag in tags:
        try:
            tag_id, value = tag.split('=')
        except ValueError:
            continue
        if tag_id not in accepted_fields:
            continue
        if tag_id == "api_key":
            device_obj = Device.objects.filter(api_key=value).first()
        elif tag_id == "Epoch":
            try:
                timestamp = dt.datetime.fromtimestamp(int(value))
            except Exception as err:
                print(str(err))
                pass
        else:
            data[fields_map[tag_id]] = value
        print(tag_id, value, timestamp)
    if device_obj != None:
        data_obj = Data(**data)
        data_obj.device = device_obj
        data_obj.timestamp = timestamp
        data_obj.save()


def rawdata_signal(sender, instance, created, **kwargs):
    if created:
        return save_to_data(instance)


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        post_save.connect(rawdata_signal, sender='base.RawPayload')
