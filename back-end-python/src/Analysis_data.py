import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
import seaborn as sns; sns.set()
import csv
from Book_extraction_single import search_for_file_path
from python_tsp.distances import great_circle_distance_matrix
from python_tsp.exact import solve_tsp_dynamic_programming
import folium
from folium import plugins
from GooglePlaces import GooglePlaces

def cluster_dots(df, base):
    
    f=0
    limit=6
    for k in range(limit):
        if k==limit-2:
                min_value=0.6
        else:
            min_value=0.4+f
        # centers=[]
        # labels=[]
        model = MeanShift()
        model.fit(df[df.columns[2:4]]) # Compute k-means clustering.
        df['cluster_label'] = model.fit_predict(df[df.columns[2:4]])
        # centers = model.cluster_centers_ # Coordinates of cluster centers.
        # labels = model.predict(df[df.columns[2:4]]) # Labels of each point
        # df.plot.scatter(x = 'LON_google', y = 'LAT_google', c=labels, s=50, cmap='viridis')
        # plt.scatter(centers[:, 1], centers[:, 0], c='black', s=200, alpha=0.2)
        # plt.title('min_value= ' + str(min_value))
        counts_clusters=df.groupby(['cluster_label']).size()
        #df=df.loc[(df['cluster_label'] !=label_cl)]
        clusters_DF=pd.DataFrame(counts_clusters)
        clusters_DF=clusters_DF.sort_values(0, ascending=[False])
        clusters_DF['normalized']=clusters_DF[0].div(clusters_DF[0].sum())
        clusters_DF["cluster_label"]=clusters_DF.index
        #print(clusters_DF.index[0])
        
        cluster_keep=[]
        z=0
        sum_val=0
        
        for i in clusters_DF['normalized']:
            sum_val=clusters_DF['normalized'][0:z].sum()

            if sum_val>min_value:
                cluster_keep.append(clusters_DF.index[0:z])
                break
            
            else:
                z+=1
        cluster_keep=pd.DataFrame(cluster_keep)
        range_1=cluster_keep.size
        datos_clustered = df[df['cluster_label'].isin(clusters_DF['cluster_label'][0:range_1])]
        #plt.scatter(centers[:, 1], centers[:, 0], c='black', s=200, alpha=0.2)
        f=f+0.1
    datos_clustered.to_csv("Data/Cleaned_data/Clustered_" + base + ".csv")
    print("saved cleaned data")
    return datos_clustered


def path_dots(df, Book_name):
    df_unicos=df.drop_duplicates(subset ="LON_google") 
    sources=df_unicos.iloc[:,3:5].values.tolist()
    distance_matrix = great_circle_distance_matrix(sources)
    Matriz_dist=pd.DataFrame(distance_matrix)
    Matriz_dist.to_csv("matriz_dist_"+ Book_name +".csv")
    new_order=[0]
    distance=[0]
    Bridge=Matriz_dist
    for i in range(len(Matriz_dist)-1):
        #index=Bridge.index[i]
        pos=new_order[i]
        Bridge=Bridge.sort_values(pos)
        new_order.append(Bridge.index[1])
        distance.append(Bridge.iloc[1][pos])
        Bridge=Bridge.drop(Bridge.index[0])
        #print(new_order, len(Bridge))
    df_unicos['new_order']=new_order
    df_unicos['distance']=distance
    df_unicos=df_unicos.reset_index()
    dat1 = pd.DataFrame([])
    for n in range(df_unicos.shape[0]):
        for m in range(df_unicos.shape[0]):
            if df_unicos.index[m] == new_order[n]:
                dat1 = dat1.append(pd.DataFrame({'LAT': df_unicos.iloc[m][4], 'LON': df_unicos.iloc[m][5], 
                'order': df_unicos.iloc[n][10], 'Distance [m]': df_unicos.iloc[n][11], 'lugares': df_unicos.iloc[m][3],
                'quotes': df_unicos.iloc[m][7], 'Position book': df_unicos.iloc[m][8]}, index=[0]), ignore_index=True)
    print("YEAH")
    dat1.to_csv("Data/Cleaned_data/Path_" + Book_name + ".csv")
    return dat1



def plot_path(dat1, Book_name):
    import folium
    from folium import plugins
    lugares3=dat1
    #ff=len(lugares3)
    # let's start again with a clean copy of the map of San Francisco
    Area = folium.Map(location=[lugares3["LAT"].iloc[0], lugares3["LON"].iloc[0]], zoom_start=12)
    Dots = plugins.MarkerCluster().add_to(Area)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, label_2, in zip(lugares3["LAT"], lugares3["LON"], lugares3["quotes"], lugares3["lugares"]):
    
        html="<b>" + label_2 +"</b>" + "<br>" + label
        iframe = folium.IFrame(html,
                       width=500,
                       height=100)    
        if type(lat)!=type(None):
            folium.Marker(
            location=[lat, lng],
            icon=folium.Icon(color='red', icon="book", prefix='fa', icon_color="white"),
            popup=folium.Popup(iframe,max_width=500),
        ).add_to(Dots)
    loc=lugares3.iloc[:,0:2]
    loc=loc.values.tolist()
    folium.PolyLine(loc, color='red', weight=10, opacity=0.5).add_to(Area)
    title_html = '''
     <head><style> html { overflow-y: hidden; } </style></head>
     <h3 align="center" style="font-size:18px"><b>Map path</b></h3>
     ''' 
    Area.get_root().html.add_child(folium.Element(title_html))
    # mini_map = plugins.MiniMap(toggle_display=True)
    # # add the mini map to the big map
    # Area.add_child(mini_map)
    Area.save('Maps/Clean_maps/Maps_path/Map_path_' + Book_name +'.html')
    return Area



def GetPlaces(api_key, location_med, type_loc, Book_name):
    
    api= GooglePlaces(api_key)
    places = api.search_places_by_coordinate(location_med, "2500", type_loc)
    #Choose fields
    fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'price_level', 'review']
    for place in places:
        #Access to details
        details = api.get_place_details(place['place_id'], fields)

    Data_Hotels=pd.DataFrame([])
    #Extract data from places dataframe
    for place in places:
        details = api.get_place_details(place['place_id'], fields)
        try:
            website = details['result']['website']
        except KeyError:
            website = ""
    
        try:
            name = details['result']['name']
        except KeyError:
            name = ""
    
        try:
            address = details['result']['formatted_address']
        except KeyError:
            address = ""
    
        try:
            phone_number = details['result']['international_phone_number']
        except KeyError:
            phone_number = ""
        

        try:
            lat = place['geometry']["location"]["lat"]
            lon = place['geometry']["location"]["lng"]

        except KeyError:
            lat = ""
            lon= ""

        try:
            rating_total = place['rating']
        
    
        except KeyError:
            rating_total=""      
          
        
        try:
            popular = place["user_ratings_total"]
    
        except KeyError:    
            popular=""
    
        try:
            reviews = details['result']['reviews']
        except KeyError:
            reviews = []
    
        Full_review=[]
        #Extract reviews per location
        for review in reviews:
            author_name = review['author_name']
            rating = review['rating']
            text = review['text']
            time = review['relative_time_description']
            #profile_photo = review['profile_photo_url']
            #Data_Hotels["Popularity"]=(popular)
            Full_review=str(Full_review) + str("Author: "+ author_name +"; Rating: "+ str(rating) +"; When: "+str(time)+ " <br> "+text + 
            "<br> NEXT <br> <br>")
        Data_Hotels= Data_Hotels.append(pd.DataFrame({'Name': name, 'Website': website, 
                'Phone Number': phone_number, 'LON': lon, 'LAT': lat,
                'Rating': rating_total, 'Popularity': popular, 'Last 5 Reviews': Full_review}, index=[0]), ignore_index=True).sort_values("Popularity", ascending=False)
        
        Data_Hotels.to_csv(type_loc + "_" + Book_name + ".csv")

    return Data_Hotels


def prova_1():
    #Output=dato+dato
    Output=("lalalalal")
    return Output