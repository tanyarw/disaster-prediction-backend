'''
        #Input 2D Arrays

        landslide_array = np.array([['location_accuracy', 'landslide_category',	'landslide_trigger', 'landslide_size', 'landslide_setting', 'country_name',	'admin_division_population','longitude','latitude']])

        rainfall_array = np.array([['month1 rainfall','month2 rainfall','month3 rainfall']]) 

        earthquake_array = np.array([['latitude', 'longitude', 'rms', 'type', 'status', 'locationSource', 'magSource', 'short place']])
        
        # Output Arrays
        
        [fatality_count] = landslide_predictor.predictor(landslide_array)
        [month4 rainfall] = rainfall_predictor.predictor(rainfall_array)
        [mag,depth, depthError] = earthquake_predictor.predictor(earthquake_array)
'''

import os
import numpy as np
from flask import Flask, flash, request, redirect, url_for
from flask_cors import CORS
import landslide_predictor
import rainfall_predictor
import earthquake_predictor

app = Flask(__name__)
CORS(app)

@app.route('/rainfallpred', methods=['GET', 'POST'])
def MakePrediction():
	if request.method == 'POST':
		posted_data = request.get_json()
		first_month = posted_data['first_month']
		second_month = posted_data['second_month']
		third_month = posted_data['third_month']
		return(str(posted_data))
        A=[first_month, second_month, third_month]
	    A = np.array(A)
	    print(A)
	    prd= rainfall_predictor.predictor(A)
	    return(str(prd))
        

if __name__=='__main__':
    app.run(debug=False)
