'''
Title: Git Data Commit
Description: This script is used to collect data from the COVID-19 Hub Feature layers hosted on ArcGIS Online into local machine and
then run the Git Commands to commit data in CSV format to this repository. 
'''

# Import the required libraries 
import pandas as pd
# from arcgis.features import GeoAccessor, GeoSeriesAccessor ==> not really using it right now
from arcgis import GIS

# intialise the GIS Object
gis = GIS()

# retrieve the Infections Times Series Layer item
infections = gis.content.get("42ec33c9361d49b585a23d780207726d")
infections_layer = infections.layers[0]

# retrieve the Vaccination Progress Times Series
vaccination = gis.content.get("0bad4380917a48da8f4f12028709c443")
vaccination_layer = vaccination.layers[2]

# retrieve the Provincial Records
provincial = gis.content.get("122efe4c5ab54ff9a9e75cc1908d48f4")
provincial_layer = provincial.layers[0]

# retrieve the Provincial Times Series Records
prov_time_series = gis.content.get("20703dd3a24f45f08ea37034285d3492")
prov_time_series_layer = prov_time_series.layers[0]

# create Spatial Dataframe objects
infections_df = pd.DataFrame.spatial.from_layer(infections_layer)
vaccination_df = pd.DataFrame.spatial.from_layer(vaccination_layer)
provincial_df = pd.DataFrame.spatial.from_layer(provincial_layer)
prov_time_series_df = pd.DataFrame.spatial.from_layer(prov_time_series_layer)

# convert the SDF to a CSV file
infections_df.to_csv(r"C:\Users\DELL\Desktop\GitHub Repositories\Zimbabwe-COVID-19-Data\time_series_data\daily_cumulative_records.csv")
vaccination_df.to_csv(r"C:\Users\DELL\Desktop\GitHub Repositories\Zimbabwe-COVID-19-Data\vaccination_progress\vaccination_metrics.csv")
provincial_df.to_csv(r"C:\Users\DELL\Desktop\GitHub Repositories\Zimbabwe-COVID-19-Data\Provincial\current_prov_stats.csv")
prov_time_series_df.to_csv(r"C:\Users\DELL\Desktop\GitHub Repositories\Zimbabwe-COVID-19-Data\time_series_data\daily_provincial_records.csv")

print("Data has been successfully updated")

# Commiting all files to GitHub
from gitpy import commitAdd, push

commitAdd("latest-data")
push()