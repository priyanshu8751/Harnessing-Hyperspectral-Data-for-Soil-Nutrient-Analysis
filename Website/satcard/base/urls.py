from django.urls import path, re_path, include
from rest_framework import routers

from base import views, viewsets


router = routers.DefaultRouter()
router.register(r'data_post', viewsets.DataPostViewset)
router.register(r'data', viewsets.DataViewset)
router.register(r'daysummary', viewsets.DaySummaryViewset)


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('device/<int:device_id>', views.DeviceView.as_view(), name='device-page'),
    re_path('api/', include(router.urls)),
    path('rawdata/', views.rawdata, name='rawdata'),
    path('reports/<int:device_id>', views.DeviceReportView.as_view(), name='device-report-page'),
    path('api/data_report/', views.get_data_report, name='data-report'),
    path('reports/', views.DeviceReportView.as_view(), name='device-report-page'),
    path('farmer_dashboard/', views.FarmerDashboard.as_view(), name='farmer-dashboard'),
    path('crop/', views.CropView.as_view(), name='crop'),
    path('satellite/', views.DeviceSatelliteView.as_view(), name='satellite'),
]