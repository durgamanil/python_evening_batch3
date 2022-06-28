# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:31:29 2022

@author: durga
"""

from tkinter import *

import tkinter as tk

window = Tk()

tk.Label(window, text="School management system",font=("Times", "50", "bold italic")).grid(column=0, row=2)
tk.Label(window, text="this is testing welcome",font="Helvetica").grid(column=0, row=4)
tk.Label(window, text="this is testing 12").grid(column=0, row=6)
tk.Label(window, text="this is testing 13").grid(column=0, row=8)
tk.Label(window, text="this is testing 14").grid(column=0, row=10)
tk.Label(window, text="this is testing 15").grid(column=0, row=12)


tk.Label(window, text="this is testing meghana").grid(column=1, row=4)
tk.Label(window, text="this is testing 12").grid(column=1, row=6)
tk.Label(window, text="this is testing 13").grid(column=1, row=8)
tk.Label(window, text="this is testing 14").grid(column=1, row=10)
tk.Label(window, text="this is testing NTR").grid(column=1, row=12)



tk.Label(window, text="this is testing charan").grid(column=2, row=4)
tk.Label(window, text="this is testing 12").grid(column=2, row=6)
tk.Label(window, text="this is testing 13").grid(column=2, row=8)
tk.Label(window, text="this is testing 14").grid(column=2, row=10)
tk.Label(window, text="this is testing Naveen").grid(column=2, row=12)

#helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")

window.mainloop()