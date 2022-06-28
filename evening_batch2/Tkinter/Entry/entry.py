# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:03:18 2022

@author: durga
"""

# =============================================================================
# entry widget
# =============================================================================


from tkinter import *

import tkinter as tk


def submit():
    name1 = name_var.get()
    print(name1)
    
#
   
window = Tk()
window.title("school management")
window.geometry("600x800")

name_var = tk.StringVar()



Label(window,text="firstname").grid(row =0,column=0)

name_entry = Entry(window,textvariable=name_var)
name_entry.grid(row =0 , column=2)

button = tk.Button(window,text="Submit",width=20,command=submit)
button.grid(row =2 , column=2)

window.mainloop()