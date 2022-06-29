# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 06:51:18 2022

@author: durga
"""

from tkinter import *


def collect_fn():
    global user_name_input_area,user_password_entry_area
    
    
    user_name1= user_name_input_area.get()
    
    user_password1 = user_password_entry_area.get()
    
    print(user_name1)
    print(user_password1)
    
    
    window1 = Tk()
    window1.geometry("450x300")
    #user_name2 = Label(top,	text = user_name1).place(x = 40,y = 60)
    #password2 = Label(top,	text = user_password1).place(x = 40,y = 100)
    
    user_name2 = Label(window1,	text = f"{user_name1}").place(x = 40,y = 60)
    password2 = Label(window1,	text = f"{user_password1}").place(x = 40,y = 100)
    
    # user_name2 = Label(window1,	text = "user_name1").place(x = 40,y = 60)
    # password2 = Label(window1,	text = "user_password1").place(x = 40,y = 100)
    
    

top = Tk()
top.geometry("450x300")
	
# the label for user_name
user_name = Label(top,	text = "Username").place(x = 40,y = 60)

# user_name = Label(top, text = "username")
# user_name.place(x=40,y=80)


# user_name = Label(top, text = "username")
# user_name.place(x=20,y=100)
	
# the label for user_password
user_password = Label(top,text = "Password").place(x = 40,y = 100)
 	

 	
user_name_input_area = Entry(top)
user_name_input_area.place(x = 110,	y = 60)
 	
user_password_entry_area = Entry(top)
user_password_entry_area.place(x = 110,	y = 100)


submit_button = Button(top,	text = "Submit",command = collect_fn).place(x = 40,y = 130)
	
top.mainloop()
