import datetime as dt

from django.core.management import BaseCommand
from django.db import IntegrityError
from django.conf import settings
from django.db.models import Avg

from base.models import DaySummary, Data, Device


class Command(BaseCommand):
    help = 'To store the average value of all parameters into day summary table'

    def add_arguments(self, parser):
        parser.add_argument('date', type=str)
        #parser.add_argument('filter_by_month', type=bool, nargs='?', default=False)

    def handle(self, *args, **options):
        date = options.get('date', None)
        if date == None:
            print("Date input is required")
        devices = Device.objects.all()
        for device in devices:
            data = Data.objects.filter(device=device, timestamp__date=date).aggregate(
                temperature_min=Avg('temperature_min'),
                temperature_max=Avg('temperature_max'),
                temperature=Avg('temperature'),
                pressure=Avg('pressure'),
                humidity=Avg('humidity'),
                irradiance=Avg('irradiance'),
                wind_speed=Avg('wind_speed'),
                wind_direction=Avg('wind_direction'),
                rainfall=Avg('rainfall')
            )

            for param in data:
                if data[param] == None:
                    continue
                obj, created = DaySummary.objects.update_or_create(
                    date=date,
                    device=device,
                    param =param,
                    defaults={"value": data[param]}
                )
                if created:
                    print("created new summary for device:{} and date:{} and param:{}".format(device, date, param))
                else:
                    print("updated new summary for device:{} and date:{} and param:{}".format(device, date, param))
