## Code to translate netCDF bathymetry files into Blender

from netCDF4 import Dataset
import numpy as np
import pandas as pd

wd = 'data/'
file = 'etopo1'
ds = Dataset(wd + file + '.nc')

ds.variables.keys()

depth = ds.variables['Band1'][:]
lat = ds.variables['lat'][:]
lon = ds.variables['lon'][:]

lonmesh, latmesh = np.meshgrid(lon, lat)

df = pd.DataFrame(columns = ['lat','lon','depth'])
df['lat'] = np.ravel(latmesh)
df['lon'] = np.ravel(lonmesh)
df['depth'] = np.ravel(depth)

df.to_csv(wd + file + '.csv', header = False, index = False)


lat
