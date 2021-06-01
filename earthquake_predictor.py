# USA EARTHQUAKES

import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Read dataset
earthquake_df = pd.read_csv('Datasets/earthquake-all-month.csv')

earthquake_df['short place']=[re.findall(r'\w+',i)[-1] for i in earthquake_df['place']]
earthquake_df.dropna(subset=['mag'],inplace=True)

# Feature vector
features=[i for i in earthquake_df.columns if earthquake_df[i].isna().sum()==0] # features include place, type and source

for i in ['mag','place','time','id','updated','net','magType']:
    features.remove(i)
    
X=earthquake_df[features]
y=earthquake_df['mag'] # predict magnitude

#Normalize the depth feature
X[['depth']] = StandardScaler().fit_transform(X[['depth']])

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
clf = RandomForestRegressor(n_estimators=100, criterion='mse', max_depth=None)
clf.fit(X_train, y_train)

def predictor(my_array):
    enc_array = my_array[0:4]
    labels = ['type', 'depthError', 'status', 'locationSource', 'magSource', 'short place']
    i = 4
    for label in labels:
        if label == 'depthError':
            enc_array.append(my_array[5])
            i +=1 
            continue
        t = label_maps[label][my_array[i]]
        i += 1
        enc_array.append(t)

    y_pred = clf.predict([enc_array])
    return y_pred[0]

def get_mae():
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    y_pred_reg = reg.predict(X_test)

    dec = DecisionTreeRegressor()
    dec.fit(X_train, y_train)
    y_pred_dec = dec.predict(X_test)

    clf = RandomForestRegressor(n_estimators=100, criterion='mse', max_depth=None)
    clf.fit(X_train, y_train)
    y_pred_clf = clf.predict(X_test)

    xgb = XGBRegressor()
    xgb.fit(X_train, y_train)
    y_pred_xgb = xgb.predict(X_test)

    return [mean_absolute_error(y_test, y_pred_reg), mean_absolute_error(y_test, y_pred_dec), mean_absolute_error(y_test, y_pred_clf), mean_absolute_error(y_test, y_pred_xgb)]