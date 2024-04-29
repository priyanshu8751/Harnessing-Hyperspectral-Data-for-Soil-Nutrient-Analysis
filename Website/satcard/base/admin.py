from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from rangefilter.filter import DateRangeFilter

from base.models import RawPayload, Data, Device, ParamGroup, DaySummary, \
    WeatherForecast, ParamConfig


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'version', 'deployment_date')


@admin.register(RawPayload)
class RawPayloadAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'payload',)


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('device', 'timestamp', 'temperature', 'irradiance', 'pressure',
                    'humidity', 'wind_speed', 'wind_direction', 'rainfall')
    list_filter = ('device',)


@admin.register(ParamGroup)
class ParamGroupAdmin(admin.ModelAdmin):
    list_display = ('params', 'title')


@admin.register(DaySummary)
class DaySummaryAdmin(admin.ModelAdmin):
    list_display = ('device', 'date', 'param', 'value')
    list_filter = ('device', 'param')


@admin.register(WeatherForecast)
class WeatherForecastAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('device', 'recorded_date', 'date', 'param', 'value')
    list_filter = ('device', 'param', ('recorded_date', DateRangeFilter),)


@admin.register(ParamConfig)
class ParamConfigAdmin(admin.ModelAdmin):
    list_display = ('param', 'unit', 'min_limit', 'max_limit', 'max_expected_delta')
    search_fields = ('param',)
