# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:04:32 2022

@author: durga
"""

from  tkinter import * 
import tkinter as tk


def print_fun():
    
    a =10
    b = 20
    print(a+b)
    print("money gives more happiness")




root = Tk()

root.geometry("400x600")
root.title("Calculator")


    
label1 = tk.Label(root,text="ATM PROJECT", font = ("Comic Sans MS",28))
label1.grid()


# button1 = tk.Button(root, text="click me",height = 5,width =30)
# button1.grid() 

button1 = tk.Button(root, text="click me" ,command= print_fun)
button1.grid(column=10, row=1) 


label1 = tk.Label(root,text="text start", font = ("Comic Sans MS",28))
label1.grid(column=10, row=10)

button1 = tk.Button(root, text="Quit" ,command= root.destroy, height = 5,width =30)
button1.grid(column=10, row=2) 


root.mainloop()




# =============================================================================
# 
# =============================================================================

from  tkinter import * 
import tkinter as tk


def print_fun():
    
    a =10
    b = 20
    print(a+b)
    print("money gives more happiness")




root = Tk()

root.geometry("400x600")
root.title("Calculator")


    
label1 = tk.Label(root,text="ATM PROJECT", font = ("Comic Sans MS",28))
label1.grid()


# button1 = tk.Button(root, text="click me",height = 5,width =30)
# button1.grid() 

button1 = tk.Button(root, text="click me" ,command= print_fun)
button1.grid(column=10, row=1) 


label1 = tk.Label(root,text="text start", font = ("Comic Sans MS",28))
label1.grid(column=5, row=1)

button1 = tk.Button(root, text="Quit" ,command= root.destroy, height = 5,width =30)
button1.grid(column=10, row=2) 


root.mainloop()


















 