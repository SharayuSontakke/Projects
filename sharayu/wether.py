import json
import tkinter as tk
from typing import Final, final
import requests
import time

def getweather(canvas):
    city=textfield.get() 
    api ="https://weather.com/en-GB/weather/today/1/51.55,-0.38"

    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    min_temp=int(json_data['main']['temp_min']-273.15)
    max_temp=int(json_data['main']['temp_max']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    Wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-21600))
    sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-21600))

    final_info=condition+"\n"+str(temp)+"◦C"
    final_data="\n"+"max temp:"+str(max_temp)+"\n"+"min temp:"+str(min_temp)+"\n"+"presure:"+str(presure)+"\n"+"humidity:"+str(humidity)+"\n"+"wind speed:"+str(Wind)+"\n"+"sunrise:"+sunrise +"\n"+"sunset:"+sunset
    l1.config(text=final_info)
    l2.config(text=final_info)

Canvas=tk.Tk()
Canvas.geometry("600x500")
Canvas.title("weather App")

f=("poppins",15,"bold")
t=("poppins",35,"bold")

textfield=tk.Entry(Canvas,font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getweather)

l1=tk.Label(Canvas,font=t)
l1.pack()
l2=tk.Label(Canvas,font=f)
l2.pack()

Canvas.mainloop()