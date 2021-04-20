# Disaster Prediction Backend

*Winter 2020-21 - CSE3020 Data Visualization - J Component Project*

## Datasets

1. NASA Landslide Catalog
2. Rainfall Dataset from Indian Government Website
3. Earthquake Dataset from the US Government Website
## Purpose

Uses a simple random forest regression classifier on the above datasets to predict the future disaster levels. The model is used to compute and deliver the data via a Flask API.

This data is visualized with a ReactJS frontend with nivo charts [here](https://github.com/sanjitk7/landslide-mitigation-frontend).

![arch](./assets/arch2.png)
## API Endpoints

1. Predict Rainfall with previous 2 months  - ***POST: /rainfallpred***
   - Sample Data to send: 
    ```
    {
        "first_month": 49.2,
        "second_month": 87.1,
        "third_month": 29.2
    }
    ```
   - Sample Output: 83.6824

2. Predict Fatality Rate given the following attributes - ***POST: /fatalitypred***
   - Sample Data to Send: 
    ```
    {
        "location_accuracy":"5km",
        "landslide_category": "mudslide",
        "landslide_trigger": "downpour",
        "landslide_size": "small",
        "landslide_setting": "unknown",
        "country_name": "United States",
        "admin_division_population": 36619.0,
        "longitude": -122.6630,
        "latitude": 45.4200
    }
    ```
   - Sample Output: [3.22222]

3. Predict magnitude of earthquake given the following attributes - ***POST: /magnitudepred***
   - Sample Data to Send:
    ```
    {
        "latitude": 33.262167,
        "longitude": -117.526000,	
        "rms": 0.17,
        "type": "earthquake",
        "status": "automatic",
        "locationSource": "ci",
        "magSource": "ci",
        "short place": "CA"
    }
    ```
    - Sample Output: 4.21223

