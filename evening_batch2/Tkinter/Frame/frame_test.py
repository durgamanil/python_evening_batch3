# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:33:41 2022

@author: durga
"""

from tkinter import *

import tkinter as tk

def top_fun():
    print("top botton pressed")

def left_fun():
    print("left botton pressed")
    
def right_fun():
    print("right botton pressed")
    
def bottom_fun():
    print("bottom botton pressed")



window = Tk()
#window.geometry("600x800")
#window.title("school management")
frame = Frame(window)
frame.pack()
#tk.Label(window, text="School management system",font=("Times", "50", "bold italic")).grid(column=0, row=2)

#tk.Label(window, text="School management system",font=("Times", "20", "bold italic")).pack()
button = tk.Button(frame,text="TOP",width=20,command=top_fun)
button.pack(side= TOP)
button = tk.Button(frame,text="LEFT",width=20,command=left_fun)
button.pack(side= LEFT)
button = tk.Button(frame,text="RIGHT",width=20,command=right_fun)
button.pack(side= RIGHT)
button = tk.Button(frame,text="BOTTOM",width=20,command=bottom_fun)
button.pack(side= BOTTOM)

window.mainloop()