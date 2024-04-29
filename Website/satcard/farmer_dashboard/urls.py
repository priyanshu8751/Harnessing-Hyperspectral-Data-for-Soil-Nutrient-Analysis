from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:device_id>/', IndexView.as_view(), name='farmer-dashboard'),
    path('<int:device_id>/wms_card/', WmsCard, name='wms-card'),
    path('<int:device_id>/map_card/', MapCard.as_view(), name='Map-card'),
    path('<int:device_id>/gdd_card/', GDDCard.as_view(), name='gdd-card'),
    path('<int:device_id>/weather/', get_weather_forecast, name='get_weather'),
    path('param_config/', views.get_param_config, name='get_param_config'),
    path('<int:device_id>/alert_card/', AlertNotifications.as_view(), name='alert-notifications'),
    path('<int:device_id>/farmer_devices/', FarmerDevicesView.as_view(), name='farmer-devices'),
     path('<int:device_id>/tasks_card/', TasksCardView.as_view(), name='tasks-card'),

] 
