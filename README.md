# bathymetry
## This is a repository for generating 3D bathymetric models with Blender from CSV or netCDF files.

#### If you're starting with a CSV file with locations and depths (see the [Florida bathymetry](https://github.com/katyabbott/bathymetry/blob/master/usgsCeCrm3_7639_0590_c1ee.csv) file for an example)
Steps (work in progress):
1. Download [CSV Mesh Importer for Blender](https://sourceforge.net/projects/csv-me-importer/) and add it as an Add-On in Blender. 
2. Open Blender and run bathymetry_with_blender.py in the Text Editor console.
3. Navigate to the View tab in the 3D Viewer window and click on "View Selected"
4. In the middle tab of the top Info panel, change "Blender Render" to "Cycles Render"
5. Change the scale so that large z values are not dominating the image and flip the y axis; I like to use x ~ 7, y ~ -7, z ~.005.
![image](https://github.com/katyabbott/bathymetry/blob/master/photos/rescale.png)
6. In the Properties console, navigate to the Material tab and start changing the color scheme. Adjust the different dropdown menus until your setup looks like the one below. Feel free to change the order of colors in your color ramp, etc.
![image](https://raw.githubusercontent.com/katyabbott/bathymetry/master/photos/material1.png)
![image](https://raw.githubusercontent.com/katyabbott/bathymetry/master/photos/material2.png)
![image](https://raw.githubusercontent.com/katyabbott/bathymetry/master/photos/material3.png)

#### If you're starting with a netCDF file:
1. First use netCDF_to_csv.py to convert your netCDF file to a CSV that conforms to the Blender input criteria. Then, follow the steps above.
