'''
        #Input 2D Arrays

        landslide_array = np.array([['location_accuracy', 'landslide_category',	'landslide_trigger', 'landslide_size', 'landslide_setting', 'country_name',	'admin_division_population','longitude','latitude']])

        rainfall_array = np.array([['month1 rainfall','month2 rainfall','month3 rainfall']]) 

        earthquake_array = np.array([['latitude', 'longitude', 'depth', 'rms', 'type', 'depthError', 'status', 'locationSource', 'magSource', 'short place']])
        
        # Output

        /rainfallpred
        MakeRainfallPrediction() => [fatality_count]      

        /fatalitypred  
        MakeFatalityPrediction() => [month_4_rainfall]

        /magnitudepred
        MakeMagnitudePrediction() => [magnitude]

        /regression
        CompareRegression() => json object
'''

import os
import numpy as np
from flask import Flask, flash, request, redirect, url_for, jsonify
from flask_cors import CORS
import landslide_predictor
import rainfall_predictor
import earthquake_predictor

app = Flask(__name__)
CORS(app)

@app.route('/rainfallpred', methods=['GET', 'POST'])
def MakeRainfallPrediction():
    if request.method == 'POST':
        posted_data = request.get_json()
        first_month = posted_data['first_month']
        second_month = posted_data['second_month']
        third_month = posted_data['third_month']
        A = [[first_month, second_month, third_month]]
        A = np.array(A)
        prd = rainfall_predictor.predictor(A)

        return(str(prd))

@app.route('/fatalitypred', methods=['GET', 'POST'])        
def MakeFatalityPrediction():
    if request.method == 'POST':
        posted_data = request.get_json()
        location_accuracy = posted_data['location_accuracy']
        landslide_category = posted_data['landslide_category']
        landslide_trigger = posted_data['landslide_trigger']
        landslide_size = posted_data['landslide_size']
        landslide_setting = posted_data['landslide_setting']
        country_name = posted_data['country_name']
        admin_division_population = posted_data['admin_division_population']
        longitude = posted_data['longitude']
        latitude = posted_data['latitude']
        A = [location_accuracy,landslide_category,landslide_trigger, landslide_size, landslide_setting, country_name,admin_division_population,longitude,latitude]
        prd = landslide_predictor.predictor(A)

        return(str(prd))

@app.route('/magnitudepred', methods=['GET', 'POST'])
def MakeMagnitudePrediction():
    if request.method == 'POST':
        posted_data = request.get_json()
        latitude = posted_data['latitude']
        longitude = posted_data['longitude']
        depth = posted_data['depth']
        rms = posted_data['rms']
        types = posted_data['type']
        depthError = posted_data['depthError']
        status = posted_data['status']
        locationSource = posted_data['locationSource']
        magSource = posted_data['magSource']
        shortPlace = posted_data['shortPlace']
        A = [latitude, longitude, depth, rms, types, depthError, status, locationSource, magSource,shortPlace]
        prd = earthquake_predictor.predictor(A)

        return(str(prd))

@app.route('/regression', methods=['GET', 'POST'])
def CompareRegression():
    if request.method == 'GET':
        reg_arr_lp = landslide_predictor.get_mae()
        reg_arr_rp = rainfall_predictor.get_mae()
        reg_arr_ep = earthquake_predictor.get_mae()

        return jsonify(
            reg_arr_lp=reg_arr_lp,
            reg_arr_rp=reg_arr_rp,
            reg_arr_ep=reg_arr_ep
        )

if __name__=='__main__':
    app.run(debug=False)
