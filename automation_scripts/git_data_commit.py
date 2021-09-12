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

# Commit the file changes to GitHub
# import base64
# from github import Github
# from github import InputGitTreeElement

# user = "Surveyor-Jr"
# password = ""
# g = Github(user,password)
# repo = g.get_user().get_repo('git-test') # repo name
# file_list = [
#     r'C:\Users\DELL\Desktop\GitHub Repositories\Zimbabwe-COVID-19-Data\time_series_data\daily_cumulative_records.csv',
#     r'C:\Users\DELL\Desktop\GitHub Repositories\Zimbabwe-COVID-19-Data\vaccination_progress\vaccination_metrics.csv',
#     r'C:\Users\DELL\Desktop\GitHub Repositories\Zimbabwe-COVID-19-Data\Provincial\current_prov_stats.csv',
#     r'C:\Users\DELL\Desktop\GitHub Repositories\Zimbabwe-COVID-19-Data\time_series_data\daily_provincial_records.csv'

# ]
# file_names = [
#     'daily_cumulative_records.csv',
#     'vaccination_metrics.csv',
#     'current_prov_stats.csv',
#     'daily_provincial_records.csv'
# ]
# commit_message = 'python automated data update'
# master_ref = repo.get_git_ref('heads/master')
# master_sha = master_ref.object.sha
# base_tree = repo.get_git_tree(master_sha)

# element_list = list()
# for i, entry in enumerate(file_list):
#     with open(entry) as input_file:
#         data = input_file.read()
#     if entry.endswith('.png'): # images must be encoded
#         data = base64.b64encode(data)
#     element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
#     element_list.append(element)

# tree = repo.create_git_tree(element_list, base_tree)
# parent = repo.get_git_commit(master_sha)
# commit = repo.create_git_commit(commit_message, tree, [parent])
# master_ref.edit(commit.sha)