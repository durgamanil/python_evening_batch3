# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:31:58 2022

@author: durga
"""

from tkinter import *

import tkinter as tk

window = Tk()
#window.geometry("600x800")
#window.title("school management")
# frame = Frame(window)
# frame.pack()



menu = Menu(window)
window.config(menu = menu)

filemenu =Menu(menu)
editmenu = Menu(menu)



menu.add_cascade(label="File",menu = filemenu)
menu.add_cascade(label="Edit",menu = editmenu)
menu.add_cascade(label="console")
menu.add_cascade(label="Run")

filemenu.add_command(label="New")
filemenu.add_command(label="open")
filemenu.add_command(label="save")


editmenu.add_command(label="copy")
editmenu.add_command(label="cut")
editmenu.add_command(label="paste")



window.mainloop()