from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("Clock")

def time():
    string=strftime('%H:%M:%S %p')
    l1.config(text=string)
    l1.after(1000,time)

l1=Label(root,font=("Algerian",80),background="black",foreground="cyan")
l1.pack(anchor='center')
time()


root.mainloop()