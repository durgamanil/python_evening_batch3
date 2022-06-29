# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:51:42 2022

@author: durga
"""


from  tkinter import * 
#from tkinter import tk
import tkinter as tk

def home_ui():
    width =600
    height = 800
    # for i in range(0,10):
    window = Tk()
    #window2 = Tk()
    window.geometry("800x600")
    #window2.geometry("700x500")
    """activebackground, activeforeground, anchor,
        background, bitmap, borderwidth, cursor,
        disabledforeground, font, foreground,
        highlightbackground, highlightcolor,
        highlightthickness, image, justify,
        padx, pady, relief, takefocus, text,
        textvariable, underline, wraplength"""

    # label1 = tk.Label(window,text="Hotel Management",bg ="pink",padx=800,pady=600)
    # label1.pack(side = tk.TOP,fill=tk.X)
    
    
 
    # label2 = tk.Label(window,text="Hotel Management",padx=0,pady=20)
    # label2.pack()
    
    tk.Button(window, text="Quit-1-0").grid(column=1, row=0)
    tk.Button(window, text="Quit-10-10",).grid(column=100, row=100)
    
    #tk.Button(window, text="Quit", command=window.destroy).grid(column=1, row=0)
    
    
    # label3 = tk.Label(window,text="Hotel Management",padx=0,pady=20)
    # label3.pack()
    # label4 = tk.Label(window,text="Hotel Management",padx=0,pady=20)
    # label4.pack()
    # label5 = tk.Label(window,te
    # label5 = tk.Label(window,text="Hotel Management",padx=0,pady=20)
    # label5.pack()
    
    window.mainloop()
    #window2.mainloo()
    
    
    


if __name__ == '__main__':
    home_ui()