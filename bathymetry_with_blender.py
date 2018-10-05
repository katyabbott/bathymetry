import bpy
import bmesh
import csv_mesh_importer as cmi 
import time

start_time = time.time()

## User input ##
filename = r"/...usgsCeCrm3_7639_0590_c1ee.csv"  #enter a valid file name here

## Delete anything already open
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()



## CSVMeshImporter code
reader = cmi.CsvLineReader(filename)
        
mesh = bpy.data.meshes.new('BathymetryMesh')
obj = bpy.data.objects.new('BathymetryObject', mesh)
        
scene = bpy.context.scene 
scene.objects.link(obj)
scene.update()
        
adder = cmi.LineMeshAdder()
adder.x_column = 0
adder.y_column = 1
adder.z_column = 2
adder.mesh = mesh
adder.make_edge = False
reader.on_line_read.add(lambda: adder.add_vertex(reader.read_numbers))
reader.on_finish.add(adder.bake)
        
reader.read()
        
## Resetting object/mesh/scene in Blender to deal with initalization issues
#bpy.ops.object.select_all(action='SELECT')  #Necessary to make edits to a mesh
scene.objects.active = bpy.data.objects['BathymetryObject']  #In order to select the object in the scene
#scene = bpy.context.scene   
bpy.ops.object.mode_set(mode='EDIT')
ob = bpy.context.object  
me = ob.data
bm = bmesh.from_edit_mesh(me)

if hasattr(bm.verts, "ensure_lookup_table"):   #Fix for older code: now Blender uses loops to access vertices
    bm.verts.ensure_lookup_table()

## Initalize variables    
prev_lat = bm.verts[0].co[0]  
dict = {prev_lat: []}


## Create dictionary with vertices indexed by latitude
for vert in bm.verts: 

	lat = vert.co[0] # latitude

	if lat == prev_lat:
		dict[prev_lat].append(vert)   # Note: This appends a vector object with lat, lon and depth

	else:
		dict[lat] = [vert]  #Create a new key

	prev_lat = lat


"""
## Optional: Check that all latitude gridlines have same number of longitude points
lon_len = len(dict[lat])
for key in dict:
    length = len(dict[key])
    if length != lon_len:
        pass
        raise Exception('Gridlines should be the same length')
"""

sorted_keys = sorted(dict.keys())  #Run through keys in order of increasing latitude
lat_len = len(sorted_keys)

## Run through each latitude line and connect faces with adjacent vertices
for i in range(lat_len - 1):
	prev_lat = dict[sorted_keys[i]]
	next_lat = dict[sorted_keys[i+1]]
	for i in range(len(prev_lat) - 1):
		if next_lat[i].co[1] == prev_lat[i].co[1]:
			bm.faces.new((prev_lat[i], prev_lat[i+1], next_lat[i + 1], next_lat[i]))

print("Elapsed time: {}".format(time.time() - start_time))

### Note: To view in Blender
# Select the mesh object. In the Transform window, change the scale to be x = 7, y = -7, z = .005 (or a similar scale to reflect magnitude of z values vs. x and y). Then in the view dropdown, select "view selected"
