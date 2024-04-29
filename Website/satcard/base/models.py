from django.db import models


class RawPayload(models.Model):
    """This stores the raw data payload received from the WMS."""
    timestamp = models.DateTimeField(auto_now=True)
    payload = models.TextField()

    def __str__(self):
    	return str(self.timestamp)


class Device(models.Model):
    """This stores the details about device WMS"""
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True, default="India")
    latitude = models.FloatField()
    longitude = models.FloatField()
    version = models.CharField(max_length=20, null=True, blank=True)
    deployment_date = models.DateField(null=True, blank=True)
    api_key = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Data(models.Model):
    """This stores the actual data of WMS"""
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temperature_min = models.FloatField(null=True, blank=True)
    temperature_max = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    irradiance = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    wind_direction = models.FloatField(null=True, blank=True)
    rainfall = models.FloatField(null=True, blank=True)
    internal_temperature = models.FloatField(null=True, blank=True)
    dp_avg = models.FloatField(null=True, blank=True)
    reset_count = models.IntegerField(null=True, blank=True)
    sm1 = models.FloatField(null=True, blank=True)
    sm2 = models.FloatField(null=True, blank=True)
    leaf_wetness = models.FloatField(null=True, blank=True)
    battery_volt = models.FloatField(null=True, blank=True)


    def __str__(self):
        return "{} : {}".format(self.device, str(self.timestamp))

    class Meta:
        unique_together = ('device', 'timestamp')
        verbose_name_plural = "Data"


class ParamGroup(models.Model):
    """This will store the configuration of how many charts to be shown and with parameter groups"""
    params = models.CharField(max_length=200, help_text="comma separated parameters")
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.params


class DaySummary(models.Model):
    """This will store the summary of parameter for each day"""
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    date = models.DateField()
    param = models.CharField(max_length=200, help_text="parameter name")
    value = models.FloatField()

    def __str__(self):
        return "{}-{}-{}".format(self.device, self.date, self.param)

    class Meta:
        unique_together = ('device', 'date', 'param')


class WeatherForecast(models.Model):
    """This will store the forecast data for a parameter"""
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    recorded_date = models.DateField()
    date = models.DateField()
    param = models.CharField(max_length=200, help_text="parameter name")
    value = models.FloatField()

    def __str__(self):
        return "{}-{}-{}".format(self.device, self.date, self.param)

    class Meta:
        unique_together = ('device', 'recorded_date', 'date', 'param')


class ParamConfig(models.Model):
    """This will store the config about a param"""
    param = models.CharField(max_length=200, help_text="parameter name", unique=True)
    unit = models.CharField(max_length=30)
    min_limit = models.FloatField()
    max_limit = models.FloatField()
    max_expected_delta = models.FloatField() # delta between 2 points

    def __str__(self):
        return self.param
