# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:26:23 2022

@author: durga
"""

from tkinter import *

import tkinter as tk

window = Tk()
window.title("school management")

#tk.Label(window, text="School management system",font=("Times", "50", "bold italic")).grid(column=0, row=2)
window.geometry("600x800")
tk.Label(window, text="School management system",font=("Times", "20", "bold italic")).grid(column=0, row=2)
button = tk.Button(window,text="STOP",width=20,command=window.destroy)
button.grid()

window.mainloop()


# =============================================================================
# 
# =============================================================================

from tkinter import *

import tkinter as tk

window = Tk()
window.title("school management")

#tk.Label(window, text="School management system",font=("Times", "50", "bold italic")).grid(column=0, row=2)
window.geometry("600x800")
tk.Label(window, text="School management system",font=("Times", "20", "bold italic")).grid(column=0, row=2)
button = tk.Button(window,text="QUIT",width=50, height= 40,command=window.destroy)
button.grid()

window.mainloop()





# =============================================================================
# 
# =============================================================================
from tkinter import *

import tkinter as tk

def print_function():
    #print("meghana")
    c = 10+20
    d = c +30
    e = d-50
    print(e)

window = Tk()
window.title("school management")

#tk.Label(window, text="School management system",font=("Times", "50", "bold italic")).grid(column=0, row=2)
window.geometry("600x800")
tk.Label(window, text="School management system",font=("Times", "20", "bold italic")).grid(column=0, row=2)
button = tk.Button(window,text="ADD",width=50, height= 40,command=print_function)
button.grid()

window.mainloop()




# =============================================================================
# 
# =============================================================================
