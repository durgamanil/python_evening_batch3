# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:08:27 2022

@author: durga
"""

from tkinter import *

import tkinter as tk

window = Tk()

#tk.Label(window, text="School management system",font=("Times", "50", "bold italic")).grid(column=0, row=2)
#window.geometry("600x800")
screen_width = window.winfo_screenwidth()
print(screen_width)

screen_height = window.winfo_screenheight()
print(screen_height)

window.mainloop()



# =============================================================================
#  title widget
# =============================================================================
from tkinter import *

import tkinter as tk

window = Tk()
window.title("school management")

#tk.Label(window, text="School management system",font=("Times", "50", "bold italic")).grid(column=0, row=2)
window.geometry("600x800")
tk.Label(window, text="School management system",font=("Times", "20", "bold italic")).grid(column=0, row=2)


window.mainloop()


# =============================================================================
# 
# =============================================================================











