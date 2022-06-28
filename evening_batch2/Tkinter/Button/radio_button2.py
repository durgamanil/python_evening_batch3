# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:45:13 2022

@author: durga
"""

from tkinter import *

import tkinter as tk

#window , root, top, mainwindows
window = Tk()

v = IntVar() 
#b = StringVar()

window.geometry("600x800")
window.title("school management")

Radiobutton(window,text="RRR",variable=v,value=1).pack()
Radiobutton(window,text="Vikram",variable=v,value=2).pack()
Radiobutton(window,text="KGF",variable=v,value=3).pack()


window.mainloop()