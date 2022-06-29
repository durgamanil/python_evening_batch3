# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 06:47:42 2022

@author: durga
"""



from tkinter import *


# create root window
root = Tk()						

# frame inside root window
frame1 = Frame(root)	
frame2 = Frame(root)				

# geometry method
frame1.grid(column =10, row =10)	
frame2.grid(column =500, row =10)						

label1 = Label(frame1,text="frame1", font = ("Comic Sans MS",28))
label1.grid()

# label1 = Label(frame1,text="frame1", font = ("Comic Sans MS",28))
# label1.grid()

# label1 = Label(frame1,text="frame1", font = ("Comic Sans MS",28))
# label1.grid()
# button inside frame which is
# inside root
button = Button(frame1, text ='Geek')
button.grid(column =10, row =10)		


label1 = Label(frame2,text="frame2", font = ("Comic Sans MS",28))
label1.grid()
button = Button(frame2, text ='Geek')
button.grid(column =10, row =20)						

# Tkinter event loop
root.mainloop()					
