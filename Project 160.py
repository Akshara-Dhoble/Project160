# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:10:44 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox
from tkinter import filedialog
import os
root = Tk()
root.title("File Dailog")

root.minsize(650,650)
root.maxsize(650,650)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
exit_image = ImageTk.PhotoImage(Image.open("exit.jpg"))
save_image = ImageTk.PhotoImage(Image.open("save.png"))

label = Label(root , text = "File Name : ")
label.place(relx=0.4 , rely=0.05, anchor=CENTER)

input_box = Entry(root )
input_box.place(relx=0.6, rely=0.05 , anchor=CENTER)

text_area = Text(root , height=35 , width=70 , bg = "silver")
text_area.place(relx=0.5 , rely=0.55, anchor=CENTER)

name = ""
def open_file() :
    global name
    text_area.delete(1.0, END)
    input_box.delete(0 , END)
    text_file = filedialog.askopenfilename(title = "Open Html File",
                                           filetypes =(("html Files" , "*.html"),))
    
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split(".")[0]
    input_box.insert(END , formated_name)
    root.title(formated_name)
    text_file = open(name , "r")
    paragraph = text_file.read()
    text_area.insert(END , paragraph)
    text_file.close()

btn_open = Button(root , image=open_image , text="Open File" , command=open_file)
btn_open.place(relx=0.1, rely=0.05 , anchor=CENTER)

btn_exit= Button(root , image=exit_image , text="Exit" , command=open_file)
btn_exit.place(relx=0.15, rely=0.05 , anchor=CENTER)

btn_save = Button(root , image=save_image , text="Save" , command=open_file)
btn_save.place(relx=0.2, rely=0.05 , anchor=CENTER)

root.mainloop()
