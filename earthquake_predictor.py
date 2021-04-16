# USA EARTHQUAKES

import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Read dataset
earthquake_df = pd.read_csv('Datasets/earthquake-all-month.csv')

earthquake_df['short place']=[re.findall(r'\w+',i)[-1] for i in earthquake_df['place']]
earthquake_df.dropna(subset=['mag'],inplace=True)

# Feature vector
features=[i for i in earthquake_df.columns if earthquake_df[i].isna().sum()==0] # features include place, type and source

for i in ['mag','place','time','id','updated','net','magType','depth','depthError']:
    features.remove(i)
    
X=earthquake_df[features]
y=earthquake_df[['mag','depth', 'depthError']] # predict magnitude, depth, depthError

# Segregate categorical data
categorical = []
for i in features:
    if earthquake_df[i].dtype=="object":
        categorical.append(i)

# Encode the data
from sklearn import preprocessing
label_maps = {}
for i in categorical:
    le = preprocessing.LabelEncoder().fit(X[i])
    X[i]=le.transform(X[i])
    d = dict(zip(le.classes_, le.transform(le.classes_)))
    label_maps[i] = d

# Train and test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.10)

# Random forest regressor
clf = RandomForestRegressor(n_estimators=100, criterion='mse', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, ccp_alpha=0.0, max_samples=None)
clf.fit(X_train, y_train)

def predictor(my_array):
    enc_array = my_array[0:3]
    labels = ['type', 'status', 'locationSource', 'magSource', 'short place']
    i = 3
    for label in labels:
        t = label_maps[label][my_array[i]]
        i += 1
        enc_array.append(t)

    y_pred = clf.predict([enc_array])
    return y_pred #['mag','depth', 'depthError'] 3 values
