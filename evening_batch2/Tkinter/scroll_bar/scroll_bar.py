# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 20:09:11 2022

@author: durga
"""


# =============================================================================
# scroll bar widget
# =============================================================================


from tkinter import *

import tkinter as tk


window = Tk()
window.geometry("200x400")
window.title("school management")

a= Scrollbar(window)
a.pack(side = RIGHT,fill=Y)

mylist1 = Listbox(window,yscrollcommand=a.set)
for line in range(100):
    mylist1.insert(END,"this is testing"+str(line))

mylist1.pack(side=LEFT,fill=BOTH)
Scrollbar().config(command=mylist1.yview)

window.mainloop()