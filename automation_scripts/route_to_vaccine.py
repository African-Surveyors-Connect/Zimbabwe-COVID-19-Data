# import API modules
from arcgis.gis import GIS
import arcgis.network as network
from arcgis.features import FeatureLayer, Feature, FeatureSet, use_proximity, FeatureCollection
from arcgis.geocoding import geocode
import pandas as pd
import time
import datetime as dt

# Imoort configuration file
from decouple import config

# Establish connection to GIS Server
gis = GIS(url='https://arcgis.com', username=config('GIS_USERNAME'), password=config('GIS_PASSWORD'))

# Get Vaccination Centers Layer
vaccination_resources = gis.content.get("f464c7f46aea483694cf2ed13e6471f4")
# retrieve only the centers
vac_centers = vaccination_resources.layers[0]

# Get the user's location
my_location = input("What is your current location?")

# geocode the user location
results = geocode(my_location)
# query the first matched result
coordinates = results[0]['location']

# get the x, y coordinates
x_coordinate = coordinates['x']
y_coordinate = coordinates['y']

# create incidence layer from user_location
incidents_json = {
                    "features": [{"attributes": {"CurbApproach": 0,
                                                 "ID": "F100086",
                                                 "Name": "User Location"},
                                  "geometry": {"x": x_coordinate, "y": y_coordinate}}
                                 ],
                    "spatialReference": {"wkid": 4326, "latestWkid": 4326},
                    "geometryType": "esriGeometryPoint",
                    "fields" : [
                        {"name" : "ID", "type" : "esriFieldTypeString", "alias" : "ID", "length" : "50"},
                        {"name" : "Name", "type" : "esriFieldTypeString", "alias" : "Name", "length" : "50"},
                        {"name" : "CurbApproach", "type" : "esriFieldTypeInteger", "alias" : "CurbApproach"}
                    ]
                }
incidents = FeatureSet.from_dict(incidents_json)

# find the closest vaccination centers
current_time = dt.datetime.now()  
result1 = network.analysis.find_closest_facilities(incidents=incidents, facilities=vac_centers, 
                                                   cutoff=25, time_of_day=current_time, 
                                                   number_of_facilities_to_find=1,
                                                   save_output_network_analysis_layer=True,
                                                   gis=gis)

# Was the tool executed successfully?
print("Is the tool executed successfully?", result1.solve_succeeded)

# Create a Spatial Dataframe
""" to create tables with valid information
"""
df4 = result1.output_routes.sdf
start_times = pd.to_datetime(df4["StartTime"], unit="ms")
end_times = pd.to_datetime(df4["EndTime"], unit="ms")
df4["StartTime"] = start_times.apply(lambda x: x.strftime("%H:%M:%S"))
df4["EndTime"] = end_times.apply(lambda x: x.strftime("%H:%M:%S"))
# df4[["Name", "StartTime", "EndTime", "IncidentID", "Total_Kilometers", "Total_Minutes"]]

# Extract keyterms from the Dataframe
start_time = df4['StartTime'][0]
end_time = df4['EndTime'][0]
distance = df4['Total_Kilometers'][0]
total_time = round(df4['Total_Minutes'][0], 2)

# print the result
print("==========Route to Nearest Vaccination Center ================")
print(f"Based on your location it will take you {total_time} minutes to travel" \
      f"to the nearest Vaccination Center which is {distance} kilometers. Your ETA" \
      f"is {end_time}")