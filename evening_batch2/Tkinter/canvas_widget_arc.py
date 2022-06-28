# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:45:58 2022

@author: durga
"""


from tkinter import *

import tkinter as tk



window = Tk()
window.title("school management")

w = Canvas(window,width =300,height=600)
w.grid()

canvas_width = 20
canvas_height = 200
y = int(canvas_height/2)
w.create_line(0,100,200,100)
w.create_arc(100, 100,200,300)

window.mainloop()