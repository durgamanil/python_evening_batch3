# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:48:55 2022

@author: durga
"""

from tkinter import *

import tkinter as tk



window = Tk()
window.title("school management")
window.geometry("600x800")

var1 = IntVar()
checkbutton1 = Checkbutton(window,text= "male",variable= var1).grid()


var2 = IntVar()
checkbutton2 = Checkbutton(window,text= "female",variable= var2).grid()

window.mainloop()




