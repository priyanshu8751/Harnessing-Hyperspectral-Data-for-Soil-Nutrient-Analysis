from django.db import models
from base.models import Device

class Farmer(models.Model):
    """Stores information about farmers."""
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='static/farmer_dashboard/assets/farmers_photo/', null=True)

    def __str__(self):
        return self.name

class CropType(models.Model):
    """Stores information about crop types."""

    KHARIF = 10
    RABI = 5

    TB_CHOICES = [
        (KHARIF, '10 for kharif'),
        (RABI, '5 for rabi')
    ]
    name = models.CharField(max_length=50, unique=True)
    # icon = models.ImageField(upload_to='crop_icons/')
    # wms_background = models.ImageField(upload_to='wms_backgrounds/')
    icon = models.ImageField(upload_to='static/farmer_dashboard/assets/crop_icons/',null=True)
    wms_background = models.ImageField(upload_to='static/farmer_dashboard/assets/wms_backgrounds/' ,null=True)
    seed_phase = models.ImageField(upload_to='static/farmer_dashboard/assets/total_growth_card/',null=True)
    seedling_phase = models.ImageField(upload_to='static/farmer_dashboard/assets/total_growth_card/',null=True)
    vegetative_phase = models.ImageField(upload_to='static/farmer_dashboard/assets/total_growth_card/',null=True)
    flowering_phase = models.ImageField(upload_to='static/farmer_dashboard/assets/total_growth_card/',null=True)
    ripening_phase = models.ImageField(upload_to='static/farmer_dashboard/assets/total_growth_card/',null=True)
    Tb = models.IntegerField(choices=TB_CHOICES, null=True, blank=True)
    seed_phase_gdd_limit = models.FloatField(null=True, blank=True)
    seedling_phase_gdd_limit = models.FloatField(null=True, blank=True)
    vegetative_phase_gdd_limit = models.FloatField(null=True, blank=True)
    flowering_phase_gdd_limit = models.FloatField(null=True, blank=True)
    ripening_phase_gdd_limit = models.FloatField(null=True, blank=True)
    has_seed_stage = models.BooleanField(default=False)
    has_seedling_stage = models.BooleanField(default=False)
    has_vegetative_stage = models.BooleanField(default=False)
    has_flowering_stage = models.BooleanField(default=False)
    has_ripening_stage = models.BooleanField(default=False)
    


    def __str__(self):
        return self.name

class Crop(models.Model):
    """Stores information about crops."""
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    crop_type = models.ForeignKey(CropType, on_delete=models.CASCADE)
    boundary_coordinates = models.TextField()
    area_covered = models.FloatField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    total_growth = models.FloatField(null=True, blank=True)
    Yield_predicted = models.FloatField(null=True, blank=True)
    date_of_planting = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True) 
    

    def __str__(self):
        return "{} - {}".format(self.farmer.name, self.name)

class GDDRecord(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='gdd_records')
    date = models.DateField()
    gdd_value = models.FloatField()

    class Meta:
        unique_together = ('crop', 'date')  # Ensure one entry per crop per day

    def __str__(self):
        return f"{self.crop.name} - {self.date} - GDD: {self.gdd_value}"

class Alert(models.Model):
    # Define the choices for alert types
    ALERT_TYPES = [
        ('Weather', 'Weather Alerts'),
        ('Irrigation', 'Irrigation Alerts'),
        ('Pest', 'Pest Alerts'),
        ('Disease', 'Disease Alerts'),
        ('Soil Health', 'Soil Health Alerts'),
        ('Equipment Maintenance', 'Equipment Maintenance Alerts'),
        ('Government Policy', 'Government Policy and Regulation Alerts'),
        ('Market Trends', 'Market Trends and News Alerts'),
        ('Harvest', 'Harvest Alerts'),
        ('Planting', 'Planting Alerts'),
        ('Heat', 'Heat Alerts'),
        ('Environmental Impact', 'Environmental Impact Alerts'),
        ('Government Support', 'Government Support Alerts'),
        ('Security', 'Security Alerts'),
        # Add other alert types as needed
    ]

    datetime = models.DateTimeField(null=True, blank=True)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='alerts')
    alert_type = models.CharField(max_length=100, choices=ALERT_TYPES)
    description = models.TextField()

    def __str__(self):
        return f"{self.get_alert_type_display()} Alert for {self.crop.name}"
    
# class Task(models.Model):
#     crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='tasks')
#     date = models.DateField()
#     task_description = models.TextField()

#     def __str__(self):
#         return f"Task for {self.crop.name} on {self.date}"

class Task(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)  # Checkbox for completion status
    completed_date = models.DateField(null=True, blank=True)  # Date the task was completed

    def __str__(self):
        return f"{self.description} - {'Completed' if self.is_completed else 'Pending'}"