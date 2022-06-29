# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 06:55:48 2022

@author: durga
"""

# =============================================================================
# Python | Add style to tkinter button
# =============================================================================
# Import Required Module
from tkinter import *
from tkinter.ttk import *

# Create Object
root = Tk()

# Set geometry (widthxheight)
root.geometry('100x100')

# This will create style object
style = Style()

# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).
style.configure('W.TButton', font =	('calibri', 10, 'bold', 'underline'),foreground = 'red')

# Style will be reflected only on
# this button because we are providing
# style only on this Button.
''' Button 1'''
btn1 = Button(root, text = 'Quit !',style = 'W.TButton',command = root.destroy)
btn1.grid(row = 0, column = 3, padx = 100)

''' Button 2'''

btn2 = Button(root, text = 'Click me !', command = None)
btn2.grid(row = 1, column = 3, pady = 10, padx = 100)

# Execute Tkinter
root.mainloop()





# =============================================================================
# 
# =============================================================================
from tkinter import *
from tkinter.ttk import *

# Create Object
root = Tk()

# Set geometry (widthxheight)
root.geometry('100x100')

# This will create style object
#style = Style()

# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).
#style.configure('W.TButton', font =	('calibri', 10, 'bold', 'underline'),foreground = 'red')

# Style will be reflected only on
# this button because we are providing
# style only on this Button.
''' Button 1'''
btn1 = Button(root, text = 'Quit !', font = ('calibri', 10, 'bold', 'underline'),foreground = 'red',command = root.destroy)
btn1.grid(row = 0, column = 3, padx = 100)

''' Button 2'''

btn2 = Button(root, text = 'Click me !', command = None)
btn2.grid(row = 1, column = 3, pady = 10, padx = 100)

# Execute Tkinter
root.mainloop()

# =============================================================================
# 
# =============================================================================
# Import Required Module
from tkinter import *
from tkinter.ttk import *

# Create Root Object
root = Tk()

# Set Geometry(widthxheight)
root.geometry('100x100')

# Create style Object
style = Style()


# Will add style to every available button
# even though we are not passing style
# to every button widget.
style.configure('TButton', font =
			('calibri', 10, 'bold', 'underline'),
				foreground = 'red')
# button 1
btn1 = Button(root, text = 'Quit !',
				style = 'TButton',
			command = root.destroy)

btn1.grid(row = 0, column = 3, padx = 100)

# button 2
btn2 = Button(root, text = 'Click me !', command = None)
btn2.grid(row = 1, column = 3, pady = 10, padx = 100)

# Execute Tkinter
root.mainloop()


# =============================================================================
# 
# =============================================================================
# Import Required Module
from tkinter import *
from tkinter.ttk import *

# Create Root Object
root = Tk()
# Set Geometry(widthxheight)
root.geometry('500x500')

# Create style Object
style = Style()

style.configure('TButton', font =
			('calibri', 20, 'bold'),
					borderwidth = '4')

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground = [('active', '!disabled', 'green')],
					background = [('active', 'black')])

# button 1
btn1 = Button(root, text = 'Quit !', command = root.destroy)
btn1.grid(row = 0, column = 3, padx = 100)

# button 2
btn2 = Button(root, text = 'Click me !', command = None)
btn2.grid(row = 1, column = 3, pady = 10, padx = 100)

# Execute Tkinter
root.mainloop()
