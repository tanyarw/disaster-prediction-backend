# GLOBAL LANDSLIDES

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Read Dataset
landslide_df = pd.read_csv('Datasets/NASA_Global_Landslide_Catalog.csv')

# Drop unwanted features

landslide_df = landslide_df.drop(['source_name', 'source_link','event_id', 'event_date','event_time',
                        'event_title', 'event_description', 'location_description','storm_name','photo_link',
                        'notes', 'event_import_source','event_import_id','country_code','submitted_date', 
                        'created_date', 'last_edited_date','admin_division_name','gazeteer_closest_point', 'gazeteer_distance','injury_count'], axis = 1)

# Drop unknown categories

to_remove = landslide_df[ (landslide_df['landslide_category'] == 'unknown') ].index
landslide_df = landslide_df.drop(to_remove)
to_remove = landslide_df[(landslide_df['location_accuracy'] == 'unknown')].index
landslide_df = landslide_df.drop(to_remove)

# Replace or drop unknown/NaN values

landslide_df = landslide_df.dropna(subset=['location_accuracy', 'landslide_category','landslide_trigger','landslide_size','landslide_setting','country_name'])

# Determine feature and target vectors
X_features = list(landslide_df.columns)
X_features.remove('fatality_count')
y = landslide_df['fatality_count']
y = y.fillna(y.median())              # deal with NaN

# One hot encoding of categorical data
encode_df = pd.get_dummies(landslide_df[X_features])
X = encode_df

# Train and test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

# Perform regression
clf = RandomForestRegressor(n_estimators=150, max_depth = None, criterion='mse')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
