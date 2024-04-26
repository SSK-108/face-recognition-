from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
from plyer import notification
import pandas as pd
import datetime
import time
def guifram2():
    time.sleep(1)
    def addstd():
        messagebox.showwarning("Note FRSAS : ","""After Adding student 
click on TRAINING 
""")
        os.system("get_faces_from_camera_tkinter.py")
    def train():
        os.system("dfeatures_extraction_to_csv.py")
    def openc():
        os.system("attendance_taker.py")
    def shdb():
        messagebox.showwarning("Note FRSAS : ","""Please use ctrl+curser 
to open the link
""")
        os.system("app.py")
    gui.configure(background='light green')
    l=Button(gui,text="ADD STUDENT",bg="blue",fg="WHITE",font=("Comic Sans MS",25),command=addstd)
    l.place(x=200,y=300)
    l=Button(gui,text="TRAINING",bg="blue",fg="WHITE",font=("Comic Sans MS",25),command=train)
    l.place(x=200,y=500)
    l=Button(gui,text="OPEN CAMERA",bg="blue",fg="WHITE",font=("Comic Sans MS",25),command=openc)
    l.place(x=700,y=300)
    l=Button(gui,text="OPEN DATABASE",bg="blue",fg="WHITE",font=("Comic Sans MS",25),command=shdb)
    l.place(x=700,y=500)

def enter():
    global n
    i=output_lab.get()
    j=input2.get()
    if i=="123" and j=="123":
        b.destroy()
        output_lab.destroy()
        input2.destroy()
        b.destroy()
        b1.destroy()
        b2.destroy()
        canvas1.destroy()
        guifram2()
    else:
        messagebox.showwarning("Warning FRSAS","""Invalid Data
Please Try Again
""")
def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=day+"-"+mont[month]+"-"+year+"   | "+time_string)
    clock.after(200,tick)
global Key
key= ''
ts =time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
day,month,year=date.split("-")
mont={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May',
      '06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
gui=Tk()
gui.geometry("1300x750")
gui.resizable(True,False)
gui.title("FRSAS")
gui.configure(background='#67eb5e')
message3 = Label(gui, text="Face Recognition system for Security & Automatic Attendance System" ,fg="white",bg="#7d350f" ,width=55 ,height=1,font=('Young Serif', 28, ' bold '))
message3.place(x=10, y=10)
clock = Label(gui,fg="orange",bg="#7d350f" ,width=55 ,height=1,font=('times', 22, ' bold '))
clock.place(x=200,y=70)
tick()
canvas1 = Canvas(gui, width=750, height=350,)
canvas1.place(x=240,y=200)
b=Label(gui,text="User ID : ",bg="white",fg="black",font="Arial 17 bold")
b.place(x=370,y=300)
user=StringVar()
output_lab=Entry(gui,textvariable=user,bg="white",fg="black",font=("Comic Sans MS",16))
output_lab.place(x=580,y=300)
out=StringVar()
b2=Label(gui,text="PASSWORD : ",bg="white",fg="black",font="Arial 17 bold")
b2.place(x=370,y=400)
input2=Entry(gui,textvariable=out,bg="white",fg="black",font=("Comic Sans MS",16))
input2.place(x=580,y=400)
b1=Button(gui,text="Log In",command=enter,fg="WHITE",font="ArialBlack 20 bold",bg="DARK blue")
b1.place(x=605,y=460)
labl=Button(gui,text="EXIT",bg="WHITE",fg="BLACK",font=("Comic Sans MS",18),command=gui.destroy)
labl.place(x=70,y=670)
gui.mainloop()
