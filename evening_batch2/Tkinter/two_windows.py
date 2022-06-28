# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:54:59 2022

@author: durga
"""
# =============================================================================
# new window generating from existing window
# =============================================================================
from tkinter import *

import tkinter as tk



def new_student_entry():
    root = Tk()
    root.geometry("200x400")
    button = tk.Button(root,text="QUIT",width=10, command=root.destroy)
    button.grid()
    root.mainloop()



window = Tk()
window.title("school management")
window.geometry("600x800")

button = tk.Button(window,text="ADD student",width=10, command=new_student_entry)
button.grid()

window.mainloop()