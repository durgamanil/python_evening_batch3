# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 07:02:18 2022

@author: durga
"""

# =============================================================================
# Python | Add image on a Tkinter button
# =============================================================================
# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Adding widgets to the root window
Label(root, text = 'GeeksforGeeks', font =('Verdana', 15)).pack(side = TOP, pady = 10)

# Creating a photoimage object to use image
photo = PhotoImage(file = r"D:\python\morning_class\tkinter\windows2.png")

# here, image option is used to
# set image on button
Button(root, text = 'Click Me !', image = photo).pack(side = TOP)

mainloop()
