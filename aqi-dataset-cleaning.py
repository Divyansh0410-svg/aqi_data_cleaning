import pandas as pd
import numpy as np

# Load the AQI dataset
aqi_data=pd.read_csv('AQI data set.csv')

#Displaying statistical summary and information about the dataset
print(aqi_data.describe())
aqi_data.info()

print()

# Check for missing values in the dataset
print('Number of null values in each column:')
print(aqi_data.isnull().sum().sort_values(ascending=False))

print()

#Checking for rows where average pollutant is 0
zero_count=(aqi_data['pollutant_avg'] == 0).sum()
print('Number of rows where average pollutant is 0: ', zero_count)

#Converting zero values in pollutant_avg column to NaN and than dropping those rows
aqi_data['pollutant_avg'] = aqi_data['pollutant_avg'].replace(0, np.nan)
aqi_data.dropna(subset=['pollutant_avg','pollutant_min','pollutant_max'], inplace=True)
    