# bathymetry
## This is a repository for generating 3D bathymetric models with Blender from CSV or netCDF files.

Steps (work in progress):
1. Open Blender and run bathymetry_with_blender.py in the Text Editor console.
2. Navigate to the View tab in the 3D Viewer window and click on "View Selected"
3. In the middle tab of the top Info panel, change "Blender Render" to "Cycles Render"
4. Change the scale so that large z values are not dominating the image and flip the y axis; I like to use x ~ 7, y ~ -7, z ~.005.
![image](https://github.com/katyabbott/bathymetry/blob/master/photos/rescale.png)
5. In the Properties console, navigate to the Material tab and start changing the color scheme. Adjust the different dropdown menus until your setup looks like the one below. Feel free to change the order of colors in your color ramp, etc.
![image](https://raw.githubusercontent.com/katyabbott/bathymetry/master/photos/material1.png)
![image](https://raw.githubusercontent.com/katyabbott/bathymetry/master/photos/material2.png)
![image](https://raw.githubusercontent.com/katyabbott/bathymetry/master/photos/material3.png)
