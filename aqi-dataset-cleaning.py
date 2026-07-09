import pandas as pd
import numpy as np

# Load the AQI dataset
aqi_data=pd.read_csv('AQI data set.csv')

""" #Displaying statistical summary and information about the dataset
print(aqi_data.describe())
aqi_data.info() """


""" #Checking for rows where average pollutant is 0
zero_count=(aqi_data['pollutant_avg'] == 0).sum()
print('Number of rows where average pollutant is 0: ', zero_count) """

#Converting zero values in pollutant_avg column to NaN and than dropping those rows
aqi_data['pollutant_avg'] = aqi_data['pollutant_avg'].replace(0, np.nan)
aqi_data.dropna(subset=['pollutant_avg','pollutant_min','pollutant_max'], inplace=True)


"""  #Verification after dropping rows
print('Total remaining rows: ', len(aqi_data))
print()
print('Number of null values in each column after dropping rows:')
print(aqi_data.isnull().sum().sort_values(ascending=False)) """

""" #Detecting unwanted space in columns
column_heads=['country','state','city','station','pollutant_id']
for col in column_heads:
    leading=aqi_data[col].astype(str).str.startswith(' ').sum()
    tailing=aqi_data[col].astype(str).str.endswith(' ').sum()
    if leading>0 or tailing>0:
        print('Column',col,'has',leading,'rows with space in front and',tailing,'rows with space at end') """ 

#Removing unwanted space from start and end in all string columns
column_heads=['country','state','city','station','pollutant_id']
for col in column_heads:
    aqi_data[col]=aqi_data[col].str.strip()

""" #Verification after removing unwantes spaces
leading=aqi_data['station'].astype(str).str.startswith(' ').sum()
tailing=aqi_data['station'].astype(str).str.endswith(' ').sum()
print('Column station','has',leading,'rows with space in front and',tailing,'rows with space at end') """

#Converting last_update column from string to datetime
aqi_data['last_update']= pd.to_datetime(aqi_data['last_update'], errors='coerce')

#Dropping rows where timestamp and critical metrics is missing
aqi_data.dropna(subset=['pollutant_max','pollutant_avg','pollutant_min','last_update'])

# =====================================
#   EXPLORATORY DATA ANALYSIS (EDA)
# =====================================
print('\n\t'+'='*40)
print('\n\t\t AIR QUALITY INSIGHT REPORT')
print('\n\t'+'='*40)

print()

#Top 5 most polluted states
pm25_states=aqi_data[aqi_data['pollutant_id'] == 'PM2.5']

#Performing analysis on states who has more than 10 monitoring stations
value_pm25=pm25_states['state'].value_counts()
valid_state=value_pm25[value_pm25>=10].index

filtered_state=pm25_states[pm25_states['state'].isin(valid_state)]

state_pm25= filtered_state.groupby('state')['pollutant_avg'].mean().sort_values(ascending=False)
print('TOP 5 MOST POLLUTED STATES OF INDIA ARE: ')
print(state_pm25.head(5))

#Most Tracked pollutants in dataset
print('\n MOST FREQUENTLY TRACKED POLLUTANTS ARE: ')
print(aqi_data['pollutant_id'].value_counts().head(3))

print()

#Highest pollution spike recorded 
max_pollution_index= aqi_data['pollutant_max'].idxmax()
max_pollution_data=aqi_data.loc[max_pollution_index]
print('State which recorded the highest pollution is',max_pollution_data['state'])
print('City which recorded the highest pollution is',max_pollution_data['city'])
print('Station which recorded the highest pollution is',max_pollution_data['station'])
print('Highest pollution recorded is',max_pollution_data['pollutant_max'])