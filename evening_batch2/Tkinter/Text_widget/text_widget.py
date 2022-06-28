# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 20:18:38 2022

@author: durga
"""

# =============================================================================
# text widget
# =============================================================================


from tkinter import *

import tkinter as tk


window = Tk()
window.geometry("200x400")
window.title("school management")

T = Text(window, height=2, width=30)
T.pack()
T.insert(END, "This is testing, meghana is working on the school management project")

window.mainloop()