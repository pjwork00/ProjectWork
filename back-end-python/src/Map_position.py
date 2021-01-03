import numpy as np
import pandas as pd
import folium
import googlemaps


def coordinates(lugares):
    #lugares_load=np.load(lugares)
    #lugares_Book=pandas.read_csv(Data_Book)
    lugares_load= lugares
    g_key=googlemaps.Client(key="AIzaSyAJ0DKhauX591z08eBbYxtcVjbFOZLfd2I")
    lugares_DF=pd.DataFrame(lugares_load)
    lugares_DF["LAT"]= None
    lugares_DF["LON"]= None
    print ("Launching Google API...")
    for i in range(0, len(lugares_DF), 1):
        geocode_result=g_key.geocode(lugares_DF.iat[i,0])
        try:
            print ("coordinates: ", i, " of ", len(lugares_DF), "extracted")
            lat=geocode_result[0]["geometry"]["location"]["lat"]
            lon=geocode_result[0]["geometry"]["location"]["lng"]
            lugares_DF.iat[i,lugares_DF.columns.get_loc("LAT")]=lat
            lugares_DF.iat[i,lugares_DF.columns.get_loc("LON")]=lon
        except:
            lat=None
            lon=None
    print ("coordinates: ", i, " extracted")
    #lugares_DF.to_csv(r'lugares.csv', index = True)
    return(lugares_DF) 

def map_points(lugares_DF):
    print("loading map...")
    Area = folium.Map(location=[lugares_DF["LAT"][0], lugares_DF["LON"][0]], zoom_start=2)
    Dots = folium.map.FeatureGroup()
    ff=len(lugares_DF)
    i=0
    # loop through the lugares points
    for lat, lng, in zip(lugares_DF["LAT"][: ff],lugares_DF["LON"][: ff]):
        if type(lugares_DF["LAT"][i])!=type(None):
            Dots.add_child(folium.features.CircleMarker([lat, lng], radius=5, color='red', fill=True, fill_color='blue', fill_opacity=0.6))
            i=i+1

# add pop-up text to each marker on the map
    latitudes = list(lugares_DF["LAT"][: ff])
    longitudes = list(lugares_DF["LON"][: ff])
    labels = list(lugares_DF[0][: ff])

    for lat, lng, label in zip(latitudes, longitudes, labels):
        if type(lat)!=type(None):
            folium.Marker([lat, lng], popup=label).add_to(Area) 
    
    return(Area.add_child(Dots))

def map_areas(lugares_DF):
    from folium import plugins
    ff=len(lugares_DF)
# let's start again with a clean copy of the map of San Francisco
    Area = folium.Map(location=[lugares_DF["LAT"][0], lugares_DF["LON"][0]], zoom_start=2)
    Dots = plugins.MarkerCluster().add_to(Area)

# loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, in zip(lugares_DF["LAT"][: ff],lugares_DF["LON"][: ff], lugares_DF[0][: ff]):
        if type(lat)!=type(None):
            folium.Marker(
            location=[lat, lng],
            icon=None,
            popup=label,
        ).add_to(Dots)

# display map
    return(Area)