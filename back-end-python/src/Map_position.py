import numpy as np
import pandas as pd
import folium
import googlemaps

def coordinates(lugares):
    #lugares_load=np.load(lugares)
    #lugares_Book=pandas.read_csv(Data_Book)
    pos, lugares_load= np.unique(lugares, return_index=True)
    g_key=googlemaps.Client(key="AIzaSyAJ0DKhauX591z08eBbYxtcVjbFOZLfd2I")
    lugares_DF=pd.DataFrame({"Position": pos, "lugares":lugares_load})
    lugares_DF["LAT_google"]= None
    lugares_DF["LON_google"]= None
    print ("Launching Google API...")
    for i in range(0, len(lugares_DF), 1):
        geocode_result=g_key.geocode(lugares_DF.iat[i,0])
        try:
            print ("coordinates: ", i, " of ", len(lugares_DF), "extracted")
            lat=geocode_result[0]["geometry"]["location"]["lat"]
            lon=geocode_result[0]["geometry"]["location"]["lng"]
            lugares_DF.iat[i,lugares_DF.columns.get_loc("LAT_google")]=lat
            lugares_DF.iat[i,lugares_DF.columns.get_loc("LON_google")]=lon
        except:
            lat=None
            lon=None
    print ("coordinates: ", i, " extracted")

    #lugares_DF.to_csv(r'lugares.csv', index = True)
    return(lugares_DF)

def Data_coord(lugares_DF, Data_Book, Book_name):  
    lugares_DF=lugares_DF.rename(columns={"Position": "lugares", "lugares": "Position"})
    lugares_DF=lugares_DF.drop(['Position'], axis=1)
    Data_Book_2=pd.merge(lugares_DF, Data_Book, on = "lugares", sort = False)
    Data_Book_2=Data_Book_2.sort_values("Position")
    Data_Book_2.to_csv("Data/Geocode_" + Book_name + ".csv")
    print("saved Data_Book_Geocode.csv")
    return(Data_Book_2)

# def map_points(lugares_DF):
#     print("loading map...")
#     Area = folium.Map(location=[Coord_DF["LAT_google"].iloc[0], Coord_DF["LON_google"].iloc[0]], zoom_start=2)
#     Dots = folium.map.FeatureGroup()
#     ff=len(lugares_DF)
#     i=0
#     # loop through the lugares points
#     for lat, lng, in zip(Coord_DF["LAT_google"].iloc[: ff],Coord_DF["LON_google"].iloc[: ff]):
#         if type(Coord_DF["LAT_google"].iloc[i])!=type(None):
#             Dots.add_child(folium.features.CircleMarker([lat, lng], radius=5, color='red', fill=True, fill_color='blue', fill_opacity=0.6))
#             i=i+1

# add pop-up text to each marker on the map
    # latitudes = list(Coord_DF["LAT_google"].iloc[: ff])
    # longitudes = list(Coord_DF["LON_google"].iloc[: ff])
    # labels = list(lugares_DF[0][: ff])

    # for lat, lng, label in zip(latitudes, longitudes, labels):
    #     if type(lat)!=type(None):
    #         folium.Marker([lat, lng], popup=label).add_to(Area) 
    
    # return(Area.add_child(Dots))

def map_areas(Coord_DF, Book_name):
    from folium import plugins
    ff=len(Coord_DF)
# let's start again with a clean copy of the map of San Francisco
    Area = folium.Map(location=[Coord_DF["LAT_google"].iloc[0], Coord_DF["LON_google"].iloc[0]], zoom_start=2)
    Dots = plugins.MarkerCluster().add_to(Area)

# loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, in zip(Coord_DF["LAT_google"].iloc[: ff],Coord_DF["LON_google"].iloc[: ff], Coord_DF["Quotes"].iloc[: ff]):
        if type(lat)!=type(None):
            folium.Marker(
            location=[lat, lng],
            icon=None,
            popup=label,
        ).add_to(Dots)
    Area.save('Maps/Map_' + Book_name +'.html')
# display map
    return()