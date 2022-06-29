# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 20:32:24 2022

@author: durga
"""

# =============================================================================
# message widget
# =============================================================================
from  tkinter import * 
#from tkinter import tk
import tkinter as tk



window6 = Tk()
window6.geometry("700x500")
print("enter user details")
label2 = tk.Label(window6,text="Welcome come to empty room info",padx=0,pady=20)
label2.grid(column=5000, row=0)
tk.Button(window6, text="Quit" ,command= window6.destroy).grid(column=900, row=100)  