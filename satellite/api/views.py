from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ModelOutputSerializer

import joblib
import ee
import tensorflow as tf
import numpy as np

ee.Authenticate()
ee.Initialize(project='ee-112001033')

def funs(latitude, longitude):
    point = ee.Geometry.Point([longitude, latitude])

    # Load Hyperion imagery
    hyperion = ee.ImageCollection("EO1/HYPERION") \
        .filterBounds(point) \
        .filterDate('2000-02-12', '2013-02-13') \
        .first()

    best_band_value = np.linspace(0, -10000, num = 40)
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            point = ee.Geometry.Point(longitude + (i / 10000), latitude + (j / 10000))
            band_values = hyperion.sample(point, 30).first()
            if(band_values.getInfo() == None):
                continue
            band_values_list = list(band_values.getInfo()['properties'].values())
            band_values_keys = [int(key[1:]) for key in band_values.getInfo()['properties'].keys()]
            if (band_values_list[20] - band_values_list[0] > best_band_value[20] - best_band_value[0]):
                best_band_value = band_values_list
    
    initial_columns1 = range(int(426.82 * 100), int(930 * 100), int(10.1836 * 100))
    initial_columns2 = range(int(912.45 * 100), int(954 * 100), int(10.09 * 100))
    initial_columns = [x / 100 for x in initial_columns1] + [x / 100 for x in initial_columns2]
    sorted_pairs = sorted(zip(initial_columns, best_band_value))
    initial_columns, y = zip(*sorted_pairs)

    target_columns = range(457, 705, 10)

    data_interpolated = np.interp(target_columns, initial_columns, y)
    
    # maintain data from 400 to 1000
    sub1 = ((2.5 * min(data_interpolated)) - max(data_interpolated)) / 1.5
    div1 = (max(data_interpolated) - sub1) / 1000
    
    sub3 = min(data_interpolated) - 400
    
    model1 = tf.keras.models.load_model("data/Nutrients_Model3")
    scaler = joblib.load('data/scaler2.save') 
    input_data_reshaped = np.reshape((data_interpolated - sub3), (-1, 25, 1))
    val4 = scaler.transform(np.reshape(data_interpolated - sub3, (-1, 25)))
    val1 = model1.predict(val4)
    
    # maintain data from 0.1 to 0.2
    sub2 = (2 * min(data_interpolated)) - max(data_interpolated)
    div2 = (max(data_interpolated) - sub2) / 0.2
    scaler = joblib.load('data/scaler.save') 
    data_interpolated1 = scaler.transform([(data_interpolated - sub2) / div2])
    
    model2 = tf.keras.models.load_model("data/Temp_mois2_Model")
    val2 = model2.predict(data_interpolated1)
    return best_band_value, list(val1[0]) + list(val2[0])


@api_view(['GET'])
def get_model_predictions(request):
    latitude = float(request.query_params.get('latitude', 0))
    longitude = float(request.query_params.get('longitude', 0))

    band_value, model_output = funs(latitude, longitude)

    # Serialize the output
    serializer = ModelOutputSerializer({'band_value': band_value, 'model_output': model_output})

    return Response(serializer.data)
