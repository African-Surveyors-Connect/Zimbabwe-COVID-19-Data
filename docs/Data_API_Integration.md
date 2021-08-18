# Data API Integration

The data hosting and applications are all based on a Geographic Information Systems framework which focuses mostly on: 

- Where?
- How?
- What?

Hence the data is in Spatial Data Format in this case `GeoJSON`. For more information read the official documentation from [geojson.org](https://geojson.org/). 

You can also get the data in formats such as `csv`, `shp` or `xlsx`. But for real-time data integration we highly recommend using the `GeoJSON` format from our Open-Data Hub. 

## For Data-Scientists

We assume most data-scientists like working with `CSV` files hence we are going to be mainly focusing on that here. 

Just a few tools which we would recommend: 

- Python
- Jupyter Notebooks 
- ArcGIS Python API

For reference in case you do not have __Python__ and __Jupyter Notebooks__ installed, you can download these from the official websites. 

Download _Python_ from [python.org](https://python.org/). As for _Jupyter Notebooks_, download a clean install of __Anaconda__ from [anaconda.com](https://anaconda.com/)

### Install ArcGIS Python API 

You require the __ArcGIS Python Library__ to be able to work with Spatial data for your analysis. This process will take you through the installation process based on the [official docs](https://developers.arcgis.com/python/guide/install-and-set-up/)

There are various ways in which you can install,  

#### Installation using Anaconda for Python Distribution

**Conda**

Open a terminal application, navigate to the directory you want to work in and activate the conda environment you want to use with the ArcGIS API for Python. Install the API with the following command:

```
conda install -c esri arcgis
```

**Pipenv**

Pipenv is the official packaging tool for managing environments and installing packages from the Python Package Index (PyPI). To install the ArcGIS API for Python from PyPI in a new environment, create a new folder named `your-folder`. Open a terminal, and run `cd /path/to/your-folder` to change directories into `your-folder`. Then, enter the following command to simultaneously create a new environment and install the API in it:

```
pipenv install arcgis
```

#### Installation as a Docker image

[Docker](https://www.docker.com/) is a popular containerization technology. Docker containers bundle software in a complete file system with everything that is needed to run it. Docker containers run the same regardless of your operating system. To learn more about docker, refer to the [official documentation](https://docs.docker.com/engine/getstarted/).

The ArcGIS API for Python is shipped as a [Docker image](https://hub.docker.com/r/esridocker/arcgis-api-python-notebook/) which you can download and power up whenever you want to use the API. These images when spun up into containers, run in an isolated environment without making any changes to your local file system.

Follow the steps below to get Docker on your computer and run the API:

- [Download docker](https://www.docker.com/products/overview) and [install](https://docs.docker.com/engine/installation/) it on your computer.
- Once installed, run the following command in terminal to pull Docker image

```
docker pull esridocker/arcgis-api-python-notebook
```

- Then spin the image into a container using the following command in terminal. Replace the `<localport>` with an available port number, for instance `8889`.

```
docker run -it -p <localport>:8888 esridocker/arcgis-api-python-notebook
```

- When the container starts, it will provide a URL (with a one time token) to open your local Notebook instance. Copy the URL and paste it in your browser's address bar to use the notebooks.

### Verify Installation

To verify your arcgis installation, run the following commands in jupyter notebook:

```python
from arcgis.gis import GIS
my_gis = GIS()
testing = my_gis.map()
testing
```

A blank map should be displayed. 

### Connecting to Spatial Data 

**Dataset Identifiers**

Just like in any other application or source, datasets have a unique identifier and in the ArcGIS Feature layers which are used for displaying COVID-19 Data, these use `Feature ID` as the unique identifier. 

The following are the `Feature ID`'s for our hosted datasets: 

*Infections Time Series* - `42ec33c9361d49b585a23d780207726d`

*Vaccination Time Series* - `0bad4380917a48da8f4f12028709c443`. 
The Vaccination Times Series contains 3 layers within the Feature Layer. For the Time Series Data query the layer with Index [2]

*Provincial Cases* - `122efe4c5ab54ff9a9e75cc1908d48f4`

*Provincial Time Series* - `20703dd3a24f45f08ea37034285d3492`. 
This one is a new introduction to the daily reporting system for COVID-19 within the Hub. 

**Importing Libraries** 

Import the relevant libraries for this exercise

```python
import pandas as pd
from arcgis.features import GeoAccessor, GeoSeriesAccessor
from arcgis import GIS
```

**Convert Spatial Data to Pandas DataFrame**

Convert the Feature Hosted layer into a Pandas DataFrame to enable querying the data using the Pandas Library

```python
gis = GIS()
item = gis.content.get("<feature_id>") # Contains the Feature ID for the Infections Time-Series layer
flayer = item.layers[0]

# create a Spatially Enabled DataFrame object
sdf = pd.DataFrame.spatial.from_layer(flayer)
sdf.head()
```

Replace the `<feature_id>` with the `ID` from the list[above](#connecting-to-spatial-data)

Take note of the `.layers[]` property. Most of the Feature layers have an index of `0` except for the _Vaccination Time Series_. 

Once the data is converted into a Dataframe you can now use `Pandas` to manipulate the data for your analysis. 

In case you want to use a software for your analysis

**Convert Dataframe to CSV File**

This will help you convert the Dataframe into a `CSV` file

```python
sdf.to_csv(r"C:\Users\<username>\Desktop\<path-to-file>\<filename>.csv")
```

Replace `<username>` with your machine username and `<path-to-file>` accordingly. 

Refer to the [Data Dictionary](Data_Dictionary.md) for a clear review of the data structure once you've downloaded


## For Web-Applications 

Querying data into your own web applications can also be achieved by specifying the parameter of your request. 

### with Python 

The method for [Connecting to Spatial Dataframe](#connecting-to-spatial-data) is still the same. Check out the process for [Data Scientists](#connecting-to-spatial-data)

But now, for querying the data let's assume we want to retrieve the latest records only. 

_Retrieve the latest number of new cases_ 

```python
largest_cum_value = sdf["Total_Cumu"].max()
latest_records = sdf.query("Total_Cumu == @largest_cum_value")
# Retrieve the Latest Records from the data
new_cases = latest_records[['New_Cases']]
print(new_cases)
```

Where `largest_cum_value` is the largest value of the Cumulative Total of Recorded Cases in the country and `Total_Cumu` is the name of the column holding the values. 

Refer to the [Data Dictionary](Data_Dictionary.md) for a clear review of the data structure. 

Instead of assuming the Cumulative Cases increase everyday and using the `Total_Cumu` as the query parameter, we could instead use the __Date__ as the parameter since each day holds a single record. 

Our query will look like: 

```python
recent_data = sdf["Date"].max()
latest_records = sdf.query("Date == @recent_data")
new_cases = latest_records[['New_Cases']]
print(new_cases)
```

### with JavaScript 

_Work in progress_ but you can check our [Contributing Guide](Contributing.md) in case you would like to contribute with a solutiuon

