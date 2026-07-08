import pandas as pd
import numpy as np

# Load the AQI dataset
aqi_data=pd.read_csv('AQI data set.csv')

#Displaying statistical summary and information about the dataset
print(aqi_data.describe())
aqi_data.info()

    