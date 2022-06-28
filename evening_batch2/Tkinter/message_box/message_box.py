# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:55:24 2022

@author: durga
"""

# =============================================================================
# Messagebox
# =============================================================================


from tkinter import *

import tkinter as tk


window = Tk()
window.geometry("600x800")
window.title("school management")

mytext = "Vandana is very good girl,naveen attending classes regularly,meghana will attend soon"
mymsg= Message(window,text=mytext)
mymsg.config(fg="red")
mymsg.pack()




# #tk.Label(window, text="School management system",font=("Times", "20", "bold italic")).pack()
# button = tk.Button(frame,text="TOP",width=20,command=top_fun)
# button.pack(side= TOP)
# button = tk.Button(frame,text="LEFT",width=20,command=left_fun)
# button.pack(side= LEFT)
# button = tk.Button(frame,text="RIGHT",width=20,command=right_fun)
# button.pack(side= RIGHT)
# button = tk.Button(bottom_frame,text="BOTTOM",width=20,command=bottom_fun)
# button.pack(side= BOTTOM)

window.mainloop()