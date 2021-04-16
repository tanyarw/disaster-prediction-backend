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

for i in ['mag','place','time','id','updated','net','magType','depth']:
    features.remove(i)
    
X=earthquake_df[features]
y=earthquake_df[['mag','depth', 'depthError']] # predict magnitude, depth, depthError

# Segregate categorical data
categorical = []
for i in features:
    if earthquake_df[i].dtype=="object":
        categorical.append(i)

# Encode the data
le = preprocessing.LabelEncoder()
for i in categorical:
    X[i]=le.fit_transform(X[i])
for i in [i for i in y.columns if y[i].dtype=='object']:
    y[i]=le.fit_transform(y[i])

# Train and test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.10)

# Random forest regressor
clf = RandomForestRegressor(n_estimators=100, criterion='mse', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, ccp_alpha=0.0, max_samples=None)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
