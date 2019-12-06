import folium
import pandas

data_sk = pandas.read_csv("slovakia_mountains.txt")
name_sk = list(data_sk['NAME'])
lat_sk = list(data_sk["LAT"])
lon_sk = list(data_sk["LON"])
elev_sk = list(data_sk["ELEV"])

data_eu = pandas.read_csv("europe_mountains.txt")
name_eu = list(data_eu["MOUNTAIN"])
lat_eu = list(data_eu["LAT"])
lon_eu = list(data_eu["LON"])
elev_eu = list(data_eu["ELEV"])

def color_producer(elevation):
	'''
	Input: datas with elevation of mountains
	Output: color symbolizing high of the mountain
	'''
	elevation = (elevation)
	if elevation < 1500:
		return 'green'
	elif 1500<=elevation>2600:
			return 'orange'
	else:
		return 'red'


map = folium.Map(location=[49.1,20.1], zoom_start=4, tiles="stamenterrain", control_scale=True)

def mountains_sk():
	'''
	INPUT: GPS coordinations(LON,LAT), elevation, name of the mountain
	OUTPUT: New layer with points and popout window including name of the mountain and elevation
	'''
	fg_sk = folium.FeatureGroup(name="Highest point in Slovakia")
	for lt, ln, el, name in zip(lat_sk,lon_sk,elev_sk,name_sk):
		fg_sk.add_child(folium.CircleMarker(location= [lt, ln], popup=name+'\n'+str(el) + "m",color ='grey', radius=8,\
		 fill_color=color_producer(el),
			fill=True,fill_opacity=0.5, weight=1))
	map.add_child(fg_sk)

def mountains_eu():
	'''
	INPUT: GPS coordinations(LON,LAT), elevation, name of the mountain
	OUTPUT: New layer with points and popout window including name of the mountain and elevation
	'''
	fg_eu = folium.FeatureGroup(name="Highest point in Europe")
	for lt, ln, el,name in zip(lat_eu,lon_eu,elev_eu,name_eu):
		fg_eu.add_child(folium.CircleMarker(location= [lt, ln], popup=name+'\n'+str(el) + "m",color ='grey', radius=8,\
		 fill_color=color_producer(el),
			fill=True,fill_opacity=0.5, weight=1))
	map.add_child(fg_eu)


mountains_sk()
mountains_eu()

map.add_child(folium.LayerControl())

#Output of this script: html file with a generated map
map.save("Map.html")