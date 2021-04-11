import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import spacy
import spacy.displacy as displacy #Text Visualization
import numpy as np  
import pandas as pd 
import re
import tkinter
from tkinter import filedialog

import os


def search_for_file_path ():
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    base=os.path.basename(tempdir)
    base=os.path.splitext(base)[0]

    return tempdir, base

# from epub to html
def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    print(len(chapters))
    print("epub to html")
    return chapters



def chap2text(chap):
    blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]
# there may be more elements you don't want, such as "style", etc.
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    
    return output

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    print("we get a txt")
    return ttext


def load_model(Book):
    print("loading NLP en_core_web_lg model...")
    nlp=spacy.load("en_core_web_lg")
    Book2=nlp(Book)
    print("loaded")
    return Book2


def listToString(s):
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 
    # Driver code     

def save_lugares(Book2):
    label=[]
    lugares=[]
    start_ent=[]
    end_ent=[]
    for ent in Book2.ents:
        if ent.label_=="GPE" or  ent.label_=="LOC" or  ent.label_=="FAC":
            lugares.append(ent.text)
            label.append(ent.label_)
            start_ent.append(ent.start_char)
            end_ent.append(ent.end_char)
        #lugares_np=np.save('lugares', lugares)
    
    return lugares, label, start_ent, end_ent


def quote_book(lugares, label, start_ent, end_ent, Book):
    #len(start_ent)
    start_frase=[]
    end_frase=[]
    for i in end_ent[::]:
        z=i
    
        while z<len(Book):
            if Book[z]==".":
            #print("finish aqui", z, i)
                end_frase.append(z)
                break
            else:
                z+=1
    
    for x in start_ent[::]:
        f=x
        while f>=0:
            if Book[f]==".":
            
                start_frase.append(f)
            #print("start aqui", f,x)
                break
            else:
                f-=1
                if f<0:
                    Null=None
                    start_frase.append(Null)
    Frases_Book=[]
    z=0
    for i in start_frase:
        Frases_clean=re.sub('\n |  |\. ', '', (Book[start_frase[z]:end_frase[z]]))
        Frases_Book.append(Frases_clean)
        z+=1
    
    Data_Book=pd.DataFrame(list(zip(lugares, label, Frases_Book)), columns=["lugares","labels", "Quotes"])
    Data_Book=pd.DataFrame(list(zip(lugares, label, Frases_Book, Data_Book.index)), columns=["lugares","labels","Quotes", "Position"])
    #Data_Book=pd.DataFrame(list(zip(Data_Book.index)), columns=["Position"])
    #Data_Book.to_csv("Data/Data_Book.csv")
    print("Quotes extracted")
    return Frases_Book, Data_Book




def show_text_ner(Book2):
    Text_entities=spacy.displacy.render(Book2, style="ent", page="true")
    return(Text_entities)
    #displacy.serve(Book2, style="ent")



