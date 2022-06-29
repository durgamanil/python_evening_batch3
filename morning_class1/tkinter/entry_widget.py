# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:42:41 2022

@author: durga
"""


# =============================================================================
# Entry
# =============================================================================

from  tkinter import * 
import tkinter as tk


def print_fun():
    global first_name
    a =10
    b = 20
    fn = first_name.get()
    print(fn)


root = Tk()

root.geometry("400x600")
root.title("Calculator")


    
label1 = tk.Label(root,text="ATM PROJECT", font = ("Comic Sans MS",28))
label1.grid()


label1 = tk.Label(root,text="Name", font = ("Comic Sans MS",28))
label1.grid(column=5, row=1)

first_name = tk.Entry(root)
first_name.grid(column=10,row=1)


# fn = first_name.get()

# print(fn)

button1 = tk.Button(root, text="clickme" ,command= print_fun, height = 5,width =30)
button1.grid(column=10, row=2) 


root.mainloop()
