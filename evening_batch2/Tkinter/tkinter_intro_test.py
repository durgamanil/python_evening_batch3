# -*- coding: utf-8 -*-
"""
Created on Sat May 28 19:15:43 2022

@author: durga
"""
import tkinter

dir(tkinter)

['ACTIVE', 'ALL',
 'ANCHOR', 'ARC',
 'BASELINE', 'BEVEL', 'BOTH',
 'BOTTOM', 'BROWSE',
 'BUTT', 'BaseWidget', 'BitmapImage',
 'BooleanVar', 'Button', 'CASCADE', 'CENTER',
 'CHAR', 'CHECKBUTTON', 'CHORD',
 'COMMAND', 'CURRENT', 'CallWrapper',
 'Canvas', 'Checkbutton', 'DISABLED',
 'DOTBOX', 'DoubleVar', 'E', 'END', 'EW', 'EXCEPTION',
 'EXTENDED', 'Entry', 'Event', 'EventType', 'FALSE',
 'FIRST', 'FLAT', 'Frame', 'GROOVE', 'Grid',
 'HIDDEN', 'HORIZONTAL', 'INSERT', 'INSIDE',
 'Image', 'IntVar', 'LAST', 'LEFT', 'Label', 'LabelFrame', 'Listbox',
 'MITER', 'MOVETO', 'MULTIPLE', 'Menu', 'Menubutton', 'Message',
 'Misc', 'N', 'NE', 'NO', 'NONE', 'NORMAL', 'NS',
 'NSEW', 'NUMERIC', 'NW', 'NoDefaultRoot', 'OFF', 'ON', 'OUTSIDE', 'OptionMenu', 'PAGES',
 'PIESLICE', 'PROJECTING', 'Pack', 'PanedWindow', 'PhotoImage', 'Place', 
 'RADIOBUTTON', 'RAISED', 'READABLE', 'RIDGE',
 'RIGHT', 'ROUND', 'Radiobutton', 'S', 'SCROLL',
 'SE', 'SEL', 'SEL_FIRST', 'SEL_LAST', 'SEPARATOR',
 'SINGLE', 'SOLID',
 'SUNKEN', 'SW', 'Scale', 'Scrollbar',
 'Spinbox', 'StringVar', 'TOP',
 'TRUE', 'Tcl', 'TclError',
 'TclVersion', 'Text', 'Tk', 'TkVersion', 'Toplevel',
 'UNDERLINE', 'UNITS', 'VERTICAL',
 'Variable', 'W', 'WORD', 'WRITABLE', 'Widget', 'Wm', 'X', 'XView', 'Y',
 'YES', 'YView', '__all__', '__builtins__', '__cached__',
 '__doc__', '__file__', '__loader__', '__name__',
 '__package__', '__path__', '__spec__', '_cnfmerge', '_default_root',
 '_exit', '_flatten', '_get_default_root',
 '_join', '_magic_re', '_setit',
 '_space_re', '_splitdict', '_stringify',
 '_support_default_root', '_test',
 '_tkerror', '_tkinter',
 '_varnum', 'commondialog',
 'constants', 'enum',
 'getboolean', 'getdouble',
 'getint', 'image_names', 'image_types',
 'mainloop', 'messagebox', 're',
 'simpledialog', 'sys', 'types', 'wantobjects']


#creating object using tkinter
main_window = tkinter.Tk()
"""statements"""
main_window.mainloop()


#syntax of label
#tk.Label(window,options)

import tkinter as tk

main_window = tkinter.Tk()
"""statements"""

tk.Label(main_window,"this is testing")

main_window.mainloop()



# =============================================================================
# label widget
# =============================================================================
from tkinter import *
from tkinter import ttk
#from tkinter import tk

window = Tk()

ttk.Label(window, text="Office management system", font ="arial").grid(column=0, row=2)
ttk.Label(window, text="Office management system").grid(column=0, row=4)
ttk.Label(window, text="Office management system").grid(column=0, row=6)
ttk.Label(window, text="Office management system").grid(column=0, row=8)
ttk.Label(window, text="Office management system").grid(column=0, row=10)
ttk.Label(window, text="Office management system").grid(column=0, row=12)

window.mainloop()



# =============================================================================
# label example2
# =============================================================================
from tkinter import *
from tkinter import ttk
#from tkinter import tk

window = Tk()

ttk.Label(window, text="Office management system", font ="arial").grid(column=0, row=2)
ttk.Label(window, text="Office management system",font ="arialblack").grid(column=0, row=4)
ttk.Label(window, text="Office management system",font ="Calibri").grid(column=0, row=6)
ttk.Label(window, text="Office management system").grid(column=0, row=8)
ttk.Label(window, text="Office management system").grid(column=0, row=10)
ttk.Label(window, text="Office management system").grid(column=0, row=12)

window.mainloop()



# =============================================================================
# 
# =============================================================================

from tkinter import *
from tkinter import ttk
#from tkinter import tk

root = Tk()

# frm = ttk.Frame(root, padding=10)
# frm.grid()
ttk.Label(root, text="Hello World!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop(


















