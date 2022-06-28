# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:24:48 2022

@author: durga
"""

from tkinter import *

import tkinter as tk


def submit():
    name1 = name_var.get()
    pass1 =pass_var.get()
    print(name1)
    print(pass1)
    window.destroy()
    
#
   
window = Tk()
window.title("school management")
window.geometry("600x800")

name_var = tk.StringVar()
pass_var = tk.StringVar()


#============================firstname==============================
Label(window,text="firstname").grid(row =0,column=0)

name_entry = Entry(window,textvariable=name_var)
name_entry.grid(row =0 , column=2)

#==============================password==============================
Label(window,text="password").grid(row =1,column=0)
pass_entry = Entry(window,textvariable=pass_var)
pass_entry.grid(row =1 , column=2)

button = tk.Button(window,text="Submit",width=20,command=submit)
button.grid(row =2 , column=2)

window.mainloop()