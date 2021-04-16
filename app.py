import os
import numpy as np
from flask import Flask, flash, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import landslide_predictor
import rainfall_predictor
import earthquake_predictor


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #2D Arrays
        my_array1 = np.array([['location_accuracy',	'landslide_category',	'landslide_trigger', 'landslide_size', 'landslide_setting', 'country_name',	'admin_division_population','longitude','latitude']])
        my_array2 = np.array([['month1','month2','month3']]) 
        my_array3 = np.array([['latitude', 'longitude', 'rms', 'type', 'status', 'locationSource', 'magSource', 'short place']])
        
        
        ans1 = landslide_predictor.predictor(my_array1)
        ans2 = rainfall_predictor.predictor(my_array2)
        ans3 = earthquake_predictor.predictor(my_array3)
        


if __name__=='__main__':
    app.run(debug=True)