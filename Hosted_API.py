import joblib
import ee
import tensorflow as tf
import numpy as np
import geemap

ee.Authenticate()
ee.Initialize(project='ee-112001033')

def funs(latitude, longitude):
        point = ee.Geometry.Point([longitude, latitude])

        # Load Hyperion imagery
        hyperion = ee.ImageCollection("EO1/HYPERION") \
            .filterBounds(point) \
            .filterDate('2000-02-12', '2013-02-13') \
            .first()

        # Create a Map object
        Map = geemap.Map(center=[latitude, longitude], zoom=12)

        # Add the Hyperion imagery to the map
        Map.addLayer(hyperion, {'bands': ['B050', 'B023', 'B015'], 'min': 1000, 'max': 14000, 'gamma': 2.5}, 'Hyperion')

        # Add a marker for the selected point
        Map.addLayer(point, {'color': 'red'}, 'Selected Point')

        best_band_value = np.linspace(0, -10000, num = 40)
        for i in range(1, 3, 2):
            print(i)
            for j in range(1, 3, 2):
                point = ee.Geometry.Point(longitude + (i / 10000), latitude + (j / 10000))
                band_values = hyperion.sample(point, 30).first()
                if(band_values.getInfo() == None):
                    continue
                band_values_list = list(band_values.getInfo()['properties'].values())
                band_values_keys = [int(key[1:]) for key in band_values.getInfo()['properties'].keys()]
                if (band_values_list[20] - band_values_list[0] > best_band_value[20] - best_band_value[0]):
                    best_band_value = band_values_list
        print(best_band_value)
        
        initial_columns1 = range(int(426.82 * 100), int(930 * 100), int(10.1836 * 100))
        initial_columns2 = range(int(912.45 * 100), int(954 * 100), int(10.09 * 100))
        initial_columns = [x / 100 for x in initial_columns1] + [x / 100 for x in initial_columns2]
        sorted_pairs = sorted(zip(initial_columns, best_band_value))
        initial_columns, y = zip(*sorted_pairs)

        target_columns = range(457, 705, 10)

        data_interpolated = np.interp(target_columns, initial_columns, y)

        print(data_interpolated)
        
        model1 = tf.keras.models.load_model("models/Nutrients_Model.keras")
        input_data_reshaped = np.reshape(data_interpolated - 1700, (-1, 25, 1))
        val1 = model1.predict(input_data_reshaped)
        
        scaler = joblib.load('models/scaler.save') 
        data_interpolated1 = scaler.transform([(data_interpolated - 1800) / 4000])
        
        model2 = tf.keras.models.load_model("models/Temp_mois2_Model.keras")
        val2 = model2.predict(data_interpolated1)
        return val1, val2

funs(27.15539, 70.10780)
