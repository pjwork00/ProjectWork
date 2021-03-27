
import pandas as pd
from Book_extraction_single import epub2text, listToString, save_lugares, load_model, show_text_ner, quote_book, search_for_file_path
from Map_position import coordinates, map_areas, Data_coord
from Analysis_data import cluster_dots, path_dots, plot_path
 


if __name__=="__main__":
    Book_path, Book_name = search_for_file_path()
    print ("\nfile_path_variable = ", Book_path)
    out=epub2text(Book_path)
    Book=(listToString(out))
    print ("Book to string")
    Book2=load_model(Book)
    print ("Model NLP loaded")  
    lugares, label, start_ent, end_ent=save_lugares(Book2)
    Quotes, Data_Book=quote_book(lugares, label, start_ent, end_ent, Book)

    lugares_DF=coordinates(lugares)
    Coord_DF=Data_coord(lugares_DF, Data_Book,  Book_name)
    map_areas(Coord_DF, Book_name)
    cluster_dots(Coord_DF, Book_name)

    
    #map_points(coord)
#Text=show_text_ner(Book2)
#print(Text)

#lugares_DF = load_lugares()

