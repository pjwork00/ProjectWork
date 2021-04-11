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
from sklearn.cluster import KMeans
api_key="AIzaSyAJ0DKhauX591z08eBbYxtcVjbFOZLfd2I"

######################################################################
######################################################################
######################################################################

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

######################################################################
######################################################################
######################################################################
def position_med(df):
    lat_med=df['LAT_google'].mean(axis=0)
    lon_med=df['LON_google'].mean(axis=0)
    lat_me=str(lat_med)
    lon_med=str(lon_med)
    location_med= lat_me + "," + lon_med
    return location_med

######################################################################
######################################################################
######################################################################

# List available HOTELS f(days)
def GetHotels(api_key, location_med, type_loc, days):
    API_values=GetPlaces(api_key, location_med, type_loc)
    Hotels=API_values.sort_values(["Popularity","Rating"], ascending=[False, False])
    Hotels=Hotels.head(days*2)
    Hotels=Hotels.reset_index(drop=True)
    return Hotels

###################################################################
######################################################################
######################################################################
# MAP for available HOTELS
def Show_hotels(Hotels):
    Hotels_AV=Hotels
    Hotels_AV.Rating=Hotels_AV.Rating.apply(str)
    Hotels_AV.Popularity=Hotels_AV.Popularity.apply(str)
    Data_Hotels=pd.DataFrame({'LAT': Hotels_AV.LAT, 'LON': Hotels_AV.LON,
        'labels': "HOTEL", 'Name': '<a href="'+ (Hotels_AV.Website)  +'"target="_blank"> ' + (Hotels_AV.Name) + ' </a>'+ 
        "<br><b>Rating: </b>" + (Hotels_AV.Rating) +
        #"<br><b>Website: </b>" + (Hotels_AV.Website) +
        "<br><b>Popularity: </b>" + (Hotels_AV.Popularity), 'Quotes': Hotels["Last 5 Reviews"]})
    Area2=[]
    from folium import plugins
    from folium.features import DivIcon
    Figure=folium.Figure(width=500, height=450)
    Area2=folium.Map(location=[Hotels["LAT"].iloc[0], Hotels["LON"].iloc[0]],
    control_scale=True, zoom_start=12)
    # Dots = plugins.MarkerCluster().add_to(Area2)
    Dots = folium.map.FeatureGroup().add_to(Area2)

    #mini_map = plugins.MiniMap(toggle_display=True)
    for lat, lng, index, label, label2 in zip(Data_Hotels["LAT"], Data_Hotels["LON"], 
    Data_Hotels.index, Data_Hotels["Name"], Data_Hotels["Quotes"]):
        # html = Data_Hotels.to_html(
        # classes="table table-striped table-hover table-condensed table-responsive")
        html="<b>Index: </b>" + str(index) + "<b><br>" + label +"</b>" + "<br>" + label2
        iframe = folium.IFrame(html, width=450, height=100)

        if type(lat)!=type(None):
                folium.Marker(
                location=[lat, lng], 
                popup=folium.Popup(iframe,max_width=500), 
                icon=folium.Icon(color='blue', icon="hotel", prefix='fa', icon_color="white")).add_to(Dots)
        #loc=lugares3.iloc[:,0:2]
        #loc=loc.values.tolist()
        #folium.PolyLine(loc, color='green', weight=10, opacity=0.7).add_to(Area)
    title_html = '''
        <head><style> html { overflow-y: hidden; } </style></head>
        <h3 align="center" style="font-size:18px"><b>Hotels</b></h3>
        ''' 
    Figure.add_child(Area2)
    Area2.get_root().html.add_child(folium.Element(title_html))
    Area2.save('Maps/Clean_maps/Maps_path/Hotels_.html')
    return(Area2)
######################################################################
######################################################################
######################################################################
def choose_hotel(Hotels, index):
    Hotel_Choosen=Hotels.iloc[index] #da aggiungere ad ogni cluster f(days)
    return Hotel_Choosen
######################################################################
######################################################################
######################################################################


def GetPOIs(api_key, location_med, type_loc, days, CLT, NAT, REC, SPEED):
    API_values=GetPlaces(api_key, location_med, type_loc)
    POIs_ext=API_values.sort_values(["Popularity","Rating"], ascending=[False, False])
    #POIs_ext = POIs_ext.applymap(str)
    POIs_ext=POIs_ext.head(days*SPEED)
    POIs_ext.Rating=POIs_ext.Rating.apply(str)
    POIs_ext.Popularity=POIs_ext.Popularity.apply(str)
    return POIs_ext
######################################################################
######################################################################
######################################################################

def path_dots(df_unicos, Book_name, Hotel_Choosen):

    df_unicos=df_unicos.append(pd.DataFrame({'LAT_google': Hotel_Choosen.LAT, 'LON_google': Hotel_Choosen.LON,
    'labels': "HOTEL", 'lugares': '<a href="'+ (Hotel_Choosen.Website)  +'"target="_blank"> ' + (Hotel_Choosen.Name) + ' </a>' +
    "<br><b>Rating: </b>" + str(Hotel_Choosen.Rating) +
    #"<br><b>Website: </b>" + (Hotel_Choosen.Website) +
    "<br><b>Popularity: </b>" + str(Hotel_Choosen.Popularity), 'Quotes': Hotel_Choosen[-1]}, index=[0]), ignore_index=True)
    df_unicos = df_unicos.iloc[np.arange(-1, len(df_unicos)-1)]
   # df_unicos = df_unicos.iloc[np.arange(-1, len(df_unicos)-1)]
    #   #Charge POIs
    #POIs_ext=POIs_ext.head(5)
   
    sources=df_unicos.iloc[:,3:5].values.tolist()
    distance_matrix = great_circle_distance_matrix(sources)
    Matriz_dist=pd.DataFrame(distance_matrix)
    #Matriz_dist.to_csv("matriz_dist_"+ Book_name +".csv")
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
                dat1 = dat1.append(pd.DataFrame({'LAT': df_unicos.LAT_google[m], 'LON': df_unicos.LON_google[m], 
                'order': df_unicos.new_order[n], 'Distance [m]': int(df_unicos.distance[n]), 'lugares': df_unicos.lugares[m],
                'quotes': df_unicos.Quotes[m], 'Position_book': df_unicos.Position[m], 'Type': df_unicos.labels[m]}, index=[0]), ignore_index=True)
    
    dat1=dat1.append(pd.DataFrame({'LAT': df_unicos.LAT_google[0], 'LON': df_unicos.LON_google[0], 
                'order': df_unicos.new_order[0], 'Distance [m]': int(df_unicos.distance[0]), 'lugares': df_unicos.lugares[0],
                'quotes': df_unicos.Quotes[0], 'Position_book': df_unicos.Position[0], 'Type': df_unicos.labels[0]}, index=[0]), ignore_index=True)

    dat1.to_csv("Data/Clean_data/Path/Path_" + Book_name + ".csv")
    print("saved")
    return dat1
######################################################################
######################################################################
######################################################################


def add_POIs_df(df, POIs_ext):
    df=df.sort_values("Position", ascending=True)
    df["Quotes_total"]="<b>" + df['Position'].astype(str) + "</b>"+ "<br>" + df['Quotes']
    df["labels"]="LIB"

    #hh=df.groupby(['LON_google']).agg(lambda col: '\n'.join(col))
    df_unicos=df.drop_duplicates(subset ="LON_google") 
    df_unicos= df_unicos.append(pd.DataFrame({'LAT_google': POIs_ext.LAT, 'LON_google': POIs_ext.LON,
    'labels': "TOUR", 'lugares': '<a href="'+ (POIs_ext.Website)  +'"target="_blank"> ' + (POIs_ext.Name) + ' </a>' +
    "<br><b>Rating: </b>" + (POIs_ext.Rating) +
    #"<br><b>Website: </b>" + (POIs_ext.Website) +
    "<br><b>Popularity: </b><br>" + (POIs_ext.Popularity), 'Quotes': POIs_ext.iloc[:,-1]}), ignore_index=True)

    s=df.assign(count=1).groupby(['LON_google','LAT_google']).agg({'count':'sum',
    'Quotes_total':lambda x : '<br>'.join(set(x))}).reset_index()
    
    for n in range(s.shape[0]):
        for m in range(s.shape[0]):
            if df_unicos["LON_google"].iloc[m] == s["LON_google"].iloc[n]:
                df_unicos["Quotes"].iloc[m] = s["Quotes_total"].iloc[n]
    
    return df_unicos
######################################################################
######################################################################
######################################################################
def plot_path(dat1, Book_name):
    import folium
    from folium import plugins
    lugares3=dat1
    #ff=len(lugares3)
    # let's start again with a clean copy of the map of San Francisco
    Figure=folium.Figure(width=550, height=550)
    
    Area = folium.Map(location=[lugares3["LAT"].iloc[0], lugares3["LON"].iloc[0]], control_scale=True, zoom_start=12)
    Dots = plugins.MarkerCluster().add_to(Area)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, label_2, typ in zip(lugares3["LAT"], lugares3["LON"], lugares3["quotes"], lugares3["lugares"],
    lugares3["Type"]):
    
        html="<b>" + label_2 +"</b>" + "<br>" + label
        iframe = folium.IFrame(html,
                       width=500,
                       height=100)
        if typ=="LIB":
            Icon= folium.Icon(color='red', icon="book", prefix='fa', icon_color="white")
        elif typ=="HOTEL":
            Icon= folium.Icon(color='blue', icon="hotel", prefix='fa', icon_color="white")  
             
        if type(lat)!=type(None):
            folium.Marker(
            location=[lat, lng],
            icon=Icon,
            popup=folium.Popup(iframe,max_width=500),
        ).add_to(Dots)
    #partenza hotel
    loc_start=lugares3.iloc[0:2,0:2]
    loc_start=loc_start.values.tolist()
    folium.PolyLine(loc_start, color='blue', weight=10, opacity=0.5).add_to(Area)
    #Percorso luoghi
    loc=lugares3.iloc[1:-1,0:2]
    loc=loc.values.tolist()
    folium.PolyLine(loc, color='red', weight=10, opacity=0.5).add_to(Area)
    #Ritorno hotel
    loc_end=lugares3.iloc[-2:-1, 0:2]
    loc_end=loc_end.append(lugares3.iloc[0:1, 0:2])
    loc_end=loc_end.values.tolist()
    folium.PolyLine(loc_end, color='blue', weight=10, opacity=0.5).add_to(Area)

    title_html = '''
     <head><style> html { overflow-y: hidden; } </style></head>
     <h3 align="center" style="font-size:18px"><b>Map path</b></h3>
     ''' 
    Figure.add_child(Area)
    Area.get_root().html.add_child(folium.Element(title_html))
    # mini_map = plugins.MiniMap(toggle_display=True)
    # # add the mini map to the big map
    # Area.add_child(mini_map)
    Area.save('Maps/Clean_maps/Maps_path/Map_path_' + Book_name +'.html')
    return Area

######################################################################
######################################################################
######################################################################

def GetPlaces(api_key, location_med, type_loc):
    
    api= GooglePlaces(api_key)
    places = api.search_places_by_coordinate(location_med, "7000", type_loc)
    #Choose fields
    fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'price_level', 'review']
    Data_places=pd.DataFrame([])
    i=0
    #Data_Hotels=[]
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
    
        # try:
        #     address = details['result']['formatted_address']
        # except KeyError:
        #     address = ""
    
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
            rating_total=0

        try:
            popular = place["user_ratings_total"]
    
        except KeyError:
            popular=0
        
        Full_review=[]
        try:
            reviews = details['result']['reviews']
           
            for review in reviews:
                author_name = review['author_name']
                rating = review['rating']
                text = review['text']
                time = review['relative_time_description']
                Full_review=str(Full_review) + str("<b>Author: </b>"+ author_name +"; <br><b>Rating: </b>"+ str(rating) +
                "<br><b>When: </b>"+str(time)+ "<br>"+text + 
                "<br><br>")
        except KeyError:
            reviews = ""
            Full_review=""
    
        i=i+1
        
        Data_places= Data_places.append(pd.DataFrame({'Name': name, 'Website': website, 
                    'Phone Number': phone_number, 'LON': lon, 'LAT': lat,
                    'Rating': rating_total, 'Popularity': popular, 'Last 5 Reviews': Full_review}, index=[0]), ignore_index=True)   
            
    return Data_places
######################################################################
######################################################################
######################################################################
def divide_days(df,days):

    dat_dummy=df
    kmeans = KMeans(n_clusters=days).fit(dat_dummy.iloc[:,3:5])
    dat_dummy["day"]=kmeans.fit_predict(dat_dummy.iloc[:,3:5])
    # centroids = kmeans.cluster_centers_
    df_by_day = dat_dummy.groupby('day')
    Schedule_day=(list(df_by_day))
    # ax=plt.scatter(dat_dummy['LON_google'], dat_dummy['LAT_google'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
    # #ax.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    # ax
    return Schedule_day
######################################################################
######################################################################
######################################################################
