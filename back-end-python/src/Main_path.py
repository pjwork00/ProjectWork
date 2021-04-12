
import pandas as pd
#from Book_extraction_single import epub2text, listToString, save_lugares, load_model, show_text_ner, quote_book, search_for_file_path
from Map_position import coordinates, map_areas, Data_coord
from Analysis_data import position_med, path_dots, GetHotels, GetPOIs, Show_hotels, choose_hotel, add_POIs_df, plot_path, divide_days
from datetime import date, time, datetime
api_key="AIzaSyAJ0DKhauX591z08eBbYxtcVjbFOZLfd2I"
Points=["lodging","bar","tourist_attraction", "restaurant", "night_club", "art", "museum", "church", "park"]


# #INPUTS
# Title_book="Angels and Demons"


# difference = finish_time - start_time
# days=difference.days
# #1 to 5
# #number of POIs choosen from the days of availability
# #Priority to popularity and ratings
# CLT=5
# #Museums, art, Churches
# NAT=1
# #Parks
# REC=2
# #Pubs, Night clubs
# #1 relax, 2 mid, 3 full speed
# #time for each visit in f(speed) and start-end points
# SPEED=3
# #BUDGET $=order POIs from lowest to highest, $$=mid, avg between all, $$$= highest
# BUDGET=2

def Itinerary_creation(Title, start_time, finish_time, CLT, NAT, REC, SPEED, BUDGET):
    start_time = date(year=2021, month=4, day=25)
    finish_time = date(year=2021, month=4, day=30)
    difference = finish_time - start_time
    days=difference.days
    path_file = "Data/Clean_data/Geocode_Geocode_Brown, Dan - Angels & Demons.csv"
    df=pd.read_csv(path_file)
    print ("Loaded data")
    location_med=position_med(df)
    #INPUT: days
    Hotels=GetHotels(api_key, location_med, "lodging", days)
    print("Hotels extracted")
    #Show on html
    Show_hotels(Hotels) #saved map on Maps/Clean_maps/Maps_path/Hotels_.html
    index=1 #Input, select hotel
    Hotel_Choosen=choose_hotel(Hotels, index) 
    
    #Get points Points["type_POI"] 
    # 1 = "bar",2 = "tourist_attraction", 3 = "restaurant", 4 = "night_club", 5 = "art", 6 = "museum", 7 = "church", 8 = "park"
    type_POI=4
    POIs_ext=GetPOIs(api_key, location_med, Points[type_POI], days, CLT, NAT, REC, SPEED) 
    print(Points[type_POI], " extracted")
    df_unicos=add_POIs_df(df, POIs_ext)

    #Divide Clusters of points per day
    Schedule_day=divide_days(df_unicos,days)

    #Select day itinerary
    day_it=0 #day 1
    Day_Points=(Schedule_day[day_it][1])
    Plan_day=path_dots(Day_Points, "Day_1_Angels", Hotel_Choosen)

    #Generate path map
    plot_path(Plan_day, Title) #Saved on Maps\Clean_maps\Maps_path\Map_path_Title_book.html

    return Plan_day


def test22(CLT, NAT, REC, SPEED, BUDGET):
    CLT=int(CLT)
    NAT=int(NAT)
    out=CLT+ NAT
    print(out)
    return out