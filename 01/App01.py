"""
Created on Sun Oct 21 00:37:57 2018

@author:Amir Taghizadeh Vahed
"""
# Reading required libraries
import pandas as pd
import numpy as np

#%%% Haversine function

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    Result =  c * r
    print('Distance', Result)


#%%% Calculating the distance between Kiruna station and Umea station


df = pd.read_csv('GoogleMapsPoints.csv',header=None)

# Renaming the columns and adding the DESCRIPTION as index for the table
df_columns = ['Latitude','Longitude','Points', 'Description']
df.columns = df_columns
df.set_index('Points', inplace=True)

x1 , y1 = df.loc['Point01',['Latitude','Longitude']]
x2 , y2 = df.loc['Point04',['Latitude','Longitude']]

haversine(x1,y1,x2,y2)
