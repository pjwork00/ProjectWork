
import pandas as pd
from Book_extraction_single import epub2text, listToString, save_lugares, load_model, show_text_ner, quote_book
from Map_position import coordinates, map_points
print("imported functions")
Book="C:\\Users\\aleja\\OneDrive\\Documents\\MBA\\99. Project Work\\Libros\\Follett, Ken - Eye of the Needle.epub"


if __name__=="__main__":
    out=epub2text(Book)
    Book=(listToString(out))
    print ("Book to string")
    Book2=load_model(Book)
    print ("Model NLP loaded")  
    lugares, label, start_ent, end_ent=save_lugares(Book2)
    Quotes, Data_Book=quote_book(lugares, label, start_ent, end_ent, Book)
    # print ("saved lugares.npy")
    
    
    
    # lugares_np="lugares.npy"
    coord=coordinates(lugares)

    frames=[Data_Book, coord["LAT"], coord["LON"]]
    Data_Book_all=pd.concat(frames, axis=1, sort=False)
    Data_Book.to_csv("Data_Book.csv")
    #map_points(coord)
#Text=show_text_ner(Book2)
#print(Text)

#lugares_DF = load_lugares()

