# farmer_dashboard/admin.py
from django.contrib import admin
from .models import Farmer, CropType, Crop, GDDRecord, Alert, Task

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']

@admin.register(CropType)
class CropTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'wms_background', 'Tb','seed_phase_gdd_limit','seedling_phase_gdd_limit','vegetative_phase_gdd_limit','flowering_phase_gdd_limit','ripening_phase_gdd_limit','has_seed_stage','has_seedling_stage','has_vegetative_stage','has_flowering_stage','has_ripening_stage']

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ['name', 'farmer', 'crop_type', 'area_covered', 'device']

@admin.register(GDDRecord)
class GDDRecordAdmin(admin.ModelAdmin):
    list_display = [ 'date', 'gdd_value']

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = [ 'crop','datetime', 'alert_type', 'description']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [ 'crop','description', 'deadline', 'is_completed', 'completed_date']