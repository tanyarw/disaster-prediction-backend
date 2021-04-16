import os
import numpy as np
from flask import Flask, flash, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import landslide_predictor
import rainfall_predictor
import earthquake_predictor
UPLOAD_FOLDER = '/Users/Tanya/Desktop/LAB/Projects/disaster-prediction-backend'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        my_array1 = np.array([])
        my_array2 = np.array(['latitude', 'longitude', 'rms', 'type', 'status', 'locationSource', 'magSource', 'short place'])
        my_array3 = np.array([])
        
        ans1 = landslide_predictor.predictor(my_array1)
        ans2 = rainfall_predictor.predictor(my_array2)
        ans3 = earthquake_predictor.predictor(my_array3)
        


if __name__=='__main__':
    app.run(debug=True)