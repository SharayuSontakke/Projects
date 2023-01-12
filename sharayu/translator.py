from tkinter import *
from PIL import Image,ImageTk
from googletrans.constants import LANGUAGES
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
from googletrans import Translator,LANGUAGES
root=Tk()
root.geometry("500x400")
root.title('Translator')
root.iconbitmap(r'C:\Users\Admin\Downloads')
root.resizable(False,False)
root.configure(bg="gray")
lan_dict={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}

def click():
    word3 = TextBlob(var1.get())
    lan=word3.detect_language()
    lan_todict= languages.get()
    lan_to=lan_dict[lan_todict]
    word3 = word3.translate(from_lang=lan,to_lang =lan_to)
    l3.configure(text=word3)
    #var2.set(word3)


def exit():
    rr=messagebox.askyesnocancel('Notification','Are you want to exit',parent=root)
    if(rr==True):
        root.destroy()
#***********************************************binding function
def on_entere1(e):
    e1['bg']="springgreen"
def on_leavee1(e):
    e1['bg']="white"

def on_entere2(e):
    e2['bg']="springgreen"
def on_leavee2(e):
    e2['bg']="white"

def on_enterb1(e):
    b1['bg']="springgreen"
def on_leaveb1(e):
    b1['bg']="white"

def on_enterb2(e):
    b2['bg']="springgreen"
def on_leaveb2(e):
    b2['bg']="white"



#********************************************************
languages=StringVar()
font_box=Combobox(root,width=30,textvariable=languages,state='readonly')
font_box['values']=[e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)

#*************************************************************
var1=StringVar()
e1=Entry(root,width=30,textvariable=var1,font=("times", 14 ,"italic bold"),relief="ridge",borderwidth=5)
e1.bind('<Enter>',on_entere1)
e1.bind('<Leave>',on_leavee1)
e1.place(x=150,y=40)

var2=StringVar()
e2=Entry(root,width=30,textvariable=var2,font=("times", 14 ,"italic bold"),relief="ridge",borderwidth=5)
e2.bind('<Enter>',on_entere2)
e2.bind('<Leave>',on_leavee2)
e2.place(x=150,y=100)
#********************************************************

l1=Label(root,text="Enter Words",font=("times", 14 ,"italic bold"),bg="gray").place(x=5,y=40)
l2=Label(root,text="Translated",font=("times", 14 ,"italic bold"),bg="gray").place(x=5,y=100)
l3=Label(root,text=" ",font=("times", 14 ,"italic bold"),bg="gray").place(x=5,y=250)
#**********************************************************
i1=PhotoImage(file='click.png')
i2=PhotoImage(file="exit.png")

i1=i1.subsample(20,20)
i2=i2.subsample(20,20)
b1=Button(root,text="Click",bd=10,bg="yellow",compound=RIGHT,image=i1,activebackground="red",
          width=100,height=40,font=("times", 14 ,"italic bold"),command=click)
b1.bind('<Enter>',on_enterb1)
b1.bind('<Leave>',on_leaveb1)
b1.place(x=70,y=170)

b2=Button(root,text="Exit",bd=10,bg="yellow",image=i2,compound=RIGHT,activebackground="red",
          width=100,height=40,font=("times", 14 ,"italic bold"),command=exit)
b2.bind('<Enter>',on_enterb2)
b2.bind('<Leave>',on_leaveb2)
b2.place(x=280,y=170)


root.mainloop()
