from tkinter import *
from tkinter import messagebox
from typing import Sized
from PIL import ImageTk,Image
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv

root=Tk()
root.geometry("900x900+400+80")
#root.resizable(False,False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")

def Record():
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq,
                        samplerate=freq,channels=2)
    
    # timer
    try:
        temp=int(duration.get())
    except:
        print("Please enter the right value")
    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1

        if(temp==0):
            messagebox.showinfo("Time Countdown","Times Up")
        Label(text=f"{str(temp)}",font="arial 40",width=4,background="#4a4a4a").place(x=800,y=400)
    sound.wait()
    write("recording.wav",freq,recording)



#icon
image_icon=PhotoImage(file='C:\\Users\\Admin\\Downloads\\microphone.png')
root.iconphoto(False,image_icon)



#logo
photo=PhotoImage(file='C:\\Users\\Admin\\Downloads\\microphone.png')
my_image=Label(image=photo,background="#4a4a4a",height=450,width=350)
my_image.pack(padx=2,pady=5)

#main
Label(text="Voice Recorder",font="arial 30 bold",background="#4a4a4a",fg="white").pack()

#entryBox
duration=StringVar()
Entry=Entry(root,textvariable=duration,font="arial 30",width=15).pack(pady=10)

Label(text="Enter Timing in Seconds...",font="arial 15",background="#4a4a4a",fg="white").pack()

#button
record=Button(root,font="arial 20",text="Record",bg="#111111",fg="white",border=0,command=Record).pack()



root.mainloop()