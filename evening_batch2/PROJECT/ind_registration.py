

# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:31:29 2022
@author: durga
file name: individual_registration_page.py
"""

from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
#from student_regiter import  student_register_fn



#functions for opening new windows
def student_registration():
    #student_register_window()
    import student_regiter
    
    
def teacher_registration():
    import teacher_register

def employee_registration():
    import employee_register
    


#def registration_details():

registration_window = Tk()
registration_window.geometry("1080x800") #("1080x800")
registration_window.title("individual registration page")


headingframe = Frame(registration_window)
headingframe.place(x=0, y=0, width=1200, height=50)
Label(headingframe, text="School management system",font=("Times", "50", "bold italic"),background="blue").place()

#print("reached upto here")
#to separate the window into block/frame
frame1 = Frame(registration_window, padx=100)
frame1.place(x=100, y=160, width=1200, height=300)


#reading the images from the folder
student_reg_image = ImageTk.PhotoImage(file ="student2.png")

teacher_reg_image = ImageTk.PhotoImage(file ="registration.png")
employee_reg_image = ImageTk.PhotoImage(file ="registration.png")
exit_image = ImageTk.PhotoImage(file ="exit.png")

#to display the image on the window
#registration image label
student_reg_image_label = Label(frame1,image= student_reg_image)
student_reg_image_label.pack(side=LEFT, padx=10)

#login image label
teacher_reg_image_label = Label(frame1,image= teacher_reg_image)
teacher_reg_image_label.pack(side=LEFT, padx=20)

employee_reg_image_label = Label(frame1,image= employee_reg_image)
employee_reg_image_label.pack(side=LEFT, padx=30)

#exit image label
exit_image_label = Label(frame1,image= exit_image)
exit_image_label.pack(side=LEFT, padx=40)


frame2  = Frame(registration_window, padx=140)
frame2.place(x=100, y=400, width=1000, height=100)

#registration
Button(frame2,text="student",pady=3,padx =50,command=student_registration).grid(column=1, row=2,padx=20)
Button(frame2,text="Teacher",pady=3,padx =50,command=teacher_registration).grid(column=2, row=2,padx=20)
Button(frame2,text="Employee",pady=3,padx =50,command=employee_registration).grid(column=3, row=2,padx=20)
Button(frame2,text="Exit",pady=3,padx =50,command=registration_window.destroy).grid(column=4, row=2,padx=20)

registration_window.mainloop()

#registration_details()
