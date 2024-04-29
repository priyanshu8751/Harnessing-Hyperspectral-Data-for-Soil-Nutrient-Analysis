import datetime as dt

import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
import emd

from django.core.management import BaseCommand
from django.db import IntegrityError
from django.conf import settings
from django.db.models import Avg, F, Min, Max

from base.models import WeatherForecast, Data, Device


class Command(BaseCommand):
    help = 'To generate and store the forecast for next 7 days for a device'

    def add_arguments(self, parser):
        #parser.add_argument('date', type=str)
        pass

    def predict(self, val_data, model_loc, what):
        #val_data = pd.read_csv(val_only)

        imf2 = emd.sift.sift(val_data[what].to_numpy())
        new_df2 = pd.DataFrame(imf2,columns=np.arange(1,imf2.shape[1]+1))
        new_df2[what] = val_data[what]
        df2=new_df2.corr("pearson")
        a = (df2[what].nlargest(2)).index[1]
        val_data["imf"] = new_df2[a]

        val_scaler = MinMaxScaler()
        df_for_vald_scaled = val_scaler.fit_transform(val_data)
        valdX = []
        valdY = []
        n_future = 1   # Number of days we want to look into the future based on the past days.
        n_past = 7  # Number of past days we want to use to predict the future.
        for i in range(n_past, len(df_for_vald_scaled) - n_future +1):
            valdX.append(df_for_vald_scaled[i - n_past:i, 0:val_data.shape[1]])
            valdY.append(df_for_vald_scaled[i + n_future - 1:i + n_future, val_data.columns.get_loc(what)])
        valdX, valdY = np.array(valdX), np.array(valdY)

        saved_model = keras.models.load_model(model_loc)

        future_predictions = []  ## list of future values
        current_batch = valdX[-1:]   ## using the last 7 days of past to predict the next future day
        for _ in range(7):    ## iterating the same for 7 days future forecast
            current_pred = saved_model.predict(current_batch)
            # print("Current_pred: {}".format(current_pred))
            # append the prediction into the array
            future_predictions.append(current_pred[0][val_data.columns.get_loc(what)])
            # use the prediction to update the batch and remove the first value
            current_batch= np.delete(current_batch,0,axis=1)
            current_pred = current_pred.reshape((1,1,9))
            current_batch = np.append(current_batch,current_pred,axis=1)
            # print("Current_batch: {}".format(current_batch))
        new = np.asarray(future_predictions,np.float64).reshape((7,1))
        future_preds = np.repeat(new,9,axis=1)
        future_preds = val_scaler.inverse_transform(future_preds)
        # print(future_preds[:,val_data.columns.get_loc(what)])
        return future_preds[:,val_data.columns.get_loc(what)]

    def save_forecast(self, device, param, recorded_date, forecast_list):
        date = recorded_date
        for item in forecast_list:
            date += dt.timedelta(days=1)
            print(date, item, param)
            if np.isnan(item):
                print("value is nan so skipping")
                continue
            obj, created = WeatherForecast.objects.update_or_create(
                device=device,
                recorded_date=recorded_date,
                date=date,
                param=param,
                defaults={"value": item}
            )
            if created:
                print("created new record for {} -> {} -> {} -> {}".format(device, recorded_date, date, param))
            else:
                print("updated record for {} -> {} -> {} -> {}".format(device, recorded_date, date, param))

    def handle(self, *args, **options):
        devices = Device.objects.all()
        base_loc = "/home/ubuntu/analytics/forecast_model/trained_models/"
        for device in devices:
            print("Device: ", device)
            data = Data.objects.filter(device=device).values(date=F('timestamp__date')).annotate(
                AVGT=Avg('temperature'),
                AVGP=Avg('pressure'),
                MAXP = Max('pressure'),
                MINP = Min('pressure'),
                MINT = Min('temperature_min'),
                MAXT = Max('temperature_max'),
                MINU = Max('humidity'),
                WINDSPD=Avg('wind_speed')
            ).order_by('date')

            if not data.exists:
                print("No data available for the device, skipping!")
                continue

            df = pd.DataFrame.from_dict(data)
            # Get date range of dataframe and fill missing values as NaN
            r = pd.date_range(start=df.date.min(), end=df.date.max())
            df = df.set_index('date').reindex(r).fillna(np.nan).rename_axis('date').reset_index()
            # fill previous value in place of NaN
            df = df.fillna(method='ffill')
            end_date = df.date.max().date()

            # Remove column name 'date'
            df = df.drop(['date'], axis=1)

            result_avgp = self.predict(df, base_loc + "AVGP/", "AVGP")
            self.save_forecast(device, "pressure_avg", end_date, result_avgp)

            result_maxp = self.predict(df, base_loc + "MAXP/", "MAXP")
            self.save_forecast(device, "pressure_max", end_date, result_maxp)

            result_minp = self.predict(df, base_loc + "MINP/", "MINP")
            self.save_forecast(device, "pressure_min", end_date, result_minp)

            result_mint = self.predict(df, base_loc + "MINT/", "MINT")
            self.save_forecast(device, "temperature_min", end_date, result_mint)

            result_maxt = self.predict(df, base_loc + "MAXT/", "MAXT")
            self.save_forecast(device, "temperature_max", end_date, result_maxt)

            result_minu = self.predict(df, base_loc + "MINU/", "MINU")
            self.save_forecast(device, "humidity_min", end_date, result_minu)

            result_windspd = self.predict(df, base_loc + "WINDSPD/", "WINDSPD")
            self.save_forecast(device, "wind_speed", end_date, result_windspd)
