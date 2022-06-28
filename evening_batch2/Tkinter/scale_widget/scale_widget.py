# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:57:38 2022

@author: durga
"""

# =============================================================================
# scale widget
# =============================================================================

from tkinter import *

import tkinter as tk


window = Tk()
window.geometry("600x800")
window.title("school management")

M = Scale(window,from_=0, to =50)
M.pack()


window.mainloop()


# =============================================================================
# Scale widget for Horizontal
# =============================================================================
from tkinter import *

import tkinter as tk


window = Tk()
window.geometry("600x800")
window.title("school management")

M = Scale(window,from_=0, to =50,orient=HORIZONTAL)
M.pack()


window.mainloop()


# =============================================================================
# vertical and Horizontal in one window
# =============================================================================
from tkinter import *

import tkinter as tk


window = Tk()
window.geometry("600x800")
window.title("school management")

M = Scale(window,from_=50, to =100)
M.pack()
M = Scale(window,from_=0, to =50,orient=HORIZONTAL)
M.pack()


window.mainloop()