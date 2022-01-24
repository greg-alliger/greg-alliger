
# Data Cleaning, QA/QC, etc.

---

## Creating New SABs


### Importing existing SABs from Source

-	Work by education level (primary, middle, high).
	-	Create a layer for each education level when digitizing or importing new SABs.
	-	Alternatively, if importing a shapefile from a trusted source (school district, county, etc.), filter by education level to only work on one level at a time.

### Digitizing new SABs from Raster


## Data Cleaning 


### Topology Checker

- Download the **Topology Checker** plugin.
- Open the plugin and choose the “wrench” icon to configure.
- Add rules for the layer you are checking.
- Standard rules used:
	- “Layer” must not have gaps.
	- “Layer” must not have invalid geometries.
	- “Layer” must not have overlaps.
- Close the configuration window.
- Run the tool by clicking the “check” icon.
- Make sure *Show errors* box is checked.

### Fix Geometries

- If “Layer” has invalid geometries, run the **Fix Geometries** tool.
	- Search **Fix Geometries** in the ***Processing Toolbox***.
	- Create a temporary layer or save to project geopackage.

### v.clean

- If “Layer” contains a field labeled “fid”, **v.clean** will not work.
	- Remove “fid” field prior to running tool.
- Choose the appropriate *Layer to Clean*.
- Leave *Input feature type* as default.
- In *Cleaning tool*, choose bpol (break polygon), rmarea (remove area), and rmdupl (remove duplicates).
	- Click the ellipsis button to enter dialogue. 
- Exit the *Cleaning tool* dialogue to main tool GUI.
- Enter 0, 0, 4 in the *Threshold* box.
	- These are the typical threshold values that I use but feel free to experiment.
	- You can tell what order the threshold values should be in by returning to the *Cleaning tool* dialogue.
		- The tools selected will now be listed in order, first on top, last on bottom.
- Check the *Combine tools with recommended follow-up tools* checkbox.
- *Grass GIS 7 Region Extent*
	- Set to layer extent of layer that is being cleaned.
- V*.in.ogr snap tolerance*
	- Can leave at default (-1).
	- Usually set between 0.0001 and 0.0003
	- May want to experiment on this value to see what works best for you.
- *V.in.ogr min area*
	- Leave at default - (0.0001).
- *Errors*
	- Uncheck *Open output file after running algorithm*.
- Leave all other parameters as default.

### Eliminate selected polygons

- After running **v.clean**, inspect your new “Cleaned” layer.
- If sliver polygons exist, select sliver polygons by their area using the **Select Features by Expression** in the selection toolbar or in the layer’s attribute table.
	- You’ll have to look at the area of a sample of your sliver polygons to determine the cutoff for selection.
	- This will be different depending on your CRS and units.
- Run the **Eliminate selected polygons** tool.
	- Choose the *Merge selection with the neighboring polygon* with the option that works best for you.

### Dissolve

- If attribute values are not ‘null’ then **Dissolve** can be used to merge the sliver polygons with the appropriate boundary.
- Choose a field from *Dissolve field(s)*.

### Topology Checker

- Reconfigure the **Topology Checker** tool for your new, cleaned layer.
- Check for overlaps, gaps, valid geometry to ensure layer is clean.

Depending on the accuracy required for your project, you may have to adjust your polygons, snap to road centerlines, etc.
- Open the **Snapping Toolbar** if it is not already open.
- Click the *Enable Topological Editing*.
	- This will move the boundaries for each touching polygon as you edit them.


## Cleaning Existing Boundaries


- Select existing boundaries that touch new SABs and export as a new layer.
- Turn on editing for this newly exported layer.
- For all education levels of the existing SABs:
	- Use the node tool to overlap entirety of the boundaries that correspond with the new SABs.
	- Use the **Difference** tool to “clip” these modified existing boundaries to the new SABs. This ensures that the boundaries are topologically correct.
		- Use the new SABs as the *Input layer* and the modified existing SABs as the *Overlay Layer*.
	- Merge this “Difference” layer with the new SABs.
	- Ensure that all the fields are properly filled out (see Add SABs Fields).


## QA for SABs


### Load from PostGIS

- In the QGIS Browser, right click on PostGIS.
	- Left click on New Connection.
- Enter your connection information (as shown in the Figure 1).
- Expand your new PostGIS connection in the Browser.
- Load census.schools.sabs_boundaries by dragging it into your map.
![how to connect to PostGIS in QGIS](https://github.com/greg-alliger/greg-alliger/blob/main/postgis_connect.png "Connect to PostGIS")

### Load new SABs

- Load SABs in QGIS that have been newly uploaded to the database (.shp, GeoPackage, etc.).
	- These are used as the “ground-truth” to test against.
	- This should be the file you created to be uploaded.

### Filter sabs_boundaries

- Right click on sabs_boundaries in the Layers list.
	- Left click on Filter…
- Filter sabs_boundaries using the “ncessch” values of new SABs.
	- Create a query like:
    
    “ncessch” in (‘120018000235’, ‘120018000233’, ‘120018000236’, …)
    
	- See Figure 2.
![filter example](https://github.com/greg-alliger/greg-alliger/blob/main/filter.png "This is how we filter")


### Detect Dataset Changes

- Search for **Detect Dataset Changes** in the ***Processing Toolbox***.
- Use the new SABs for *Original Layer*.
- Use the the filtered “sabs_boundaries” as the *Revised Layer*.
- Chose “ncessch” field for *Attributes to consider for match (or none to compare geometry only)*.
- In Advanced Parameters:
	- For *Geometry comparison* behavior chose Exact Match.
- Leave only *Deleted Features* checked for *Open output file after running algorithm*.
- If any features exist in the new “Deleted” layer, they were not uploaded to the database correctly.
