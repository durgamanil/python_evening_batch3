# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:31:29 2022

@author: durga
"""

from tkinter import *

import tkinter as tk

window = Tk()

tk.Label(window, text="School management system",font=("Times", "50", "bold italic"),background="blue").grid(column=0, row=2)


#registration
button = tk.Button(window,text="Registration",width=20,command=window.destroy)
button.grid(column=2, row=2)

#login
button = tk.Button(window,text="Login",width=20,command=window.destroy)
button.grid(column=4, row=2)

#exit
button = tk.Button(window,text="Exit",width=20,command=window.destroy)
button.grid(column=6, row=2)


window.mainloop()