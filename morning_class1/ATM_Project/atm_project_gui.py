# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 06:46:57 2022

@author: durga
"""

# =============================================================================
# importing the required libraries
# =============================================================================
try:
        
    from tkinter import *
    from tkinter.ttk import *
    #import tensorflow
    import os
    import sys
    import pymysql
    
    
except Exception as err:
    print("library import error",err)
    sys.exit()
 
    
# =============================================================================
# connecting with mysql database
# =============================================================================
try:
    print("connecting with the mysql database")
    conn = pymysql.connect(host='localhost',user='root',password = "",db='atm_project')
    cursor1 = conn.cursor()
    print(cursor1)
    
except Exception as err:
    print("library import error",err)
    sys.exit()
    
    
# =============================================================================
# how to check the tables
# =============================================================================
# conn = pymysql.connect(host='localhost',user='root',password = "",db='atm_project')
# cursor1 = conn.cursor()
# #print(cursor1)

try :
    cursor1.execute("SHOW TABLES")
    #print(cursor1)
    for i in cursor1:
        print(i)
        
except Exception as err:
    print("table are not existing error",err)
    sys.exit()
    

# =============================================================================
# display data of the tables
# =============================================================================

# cursor1.execute("SELECT * FROM customers_data")
# for i in cursor1:
#     print(i)



# =============================================================================
# to read special columns
# =============================================================================
# cursor1.execute("SELECT ATM_card_num FROM customers_data")
# for i in cursor1:
#     print(i)


# =============================================================================
# inserting the data into tables
# =============================================================================
# conn = pymysql.connect(host='localhost',user='root',password = "",db='kumar2')
# cursor1 = conn.cursor()
# print(cursor1)

# try :
    
#     sql = "INSERT INTO customers_data (Customer_id,Customer_name,Father_name,Mother_name,ATM_card_num,password) VALUES (%d, %s,%s,%s,%d,%d)"
#     val = ("ramcharan", "chiranjivi","teacher")
#INSERT INTO `customers_data` (`S.no`, `Customer_id`, `Customer_name`, `Father_name`, `Mother_name`, `ATM_card_num`, `password`) VALUES (NULL, '2022040901', 'ram charan', 'chiranjivi', 'subbammma', '1234456712', '3636');
#     cursor1.execute(sql, val)
    
#     conn.commit()
    
# except Exception as err:
#     print("inserting data into table is failed",err)
#     sys.exit()


def cash_dispense():
    try:
        cursor1.execute("SELECT Total_cash FROM cash_details")
        for i in cursor1:
            print("Total cash",i)
            #card_exist =i
        
    
    except Exception as err:
        print("unable to dispense cash ",err)
        sys.exit()
        
    
def password_verify():
     try:
         #global pin_num
         pin_verify = pin_num.get()
         print(pin_verify)
         pin_verify2 = int(pin_verify)
         print(type(pin_verify2))
         
         cursor1.execute("SELECT password FROM customers_data")
         for i in cursor1:
             print("password",i)
             #print(type(i[0]))
             pin_match2 = i[0]
             
         
         if pin_verify2 == pin_match2:
             print("pin is matched")
             cash_dispense()
        
         else:
             label = Label(password_window, text = "entered pin is wrong", font = ("Arial Black",20))
             label.grid(row = 15, column = 10, padx = 100)
             
             
             
         
     except Exception as err:
         print("entered pin does not match ",err)
         sys.exit()
         
    

def password_entry():
    
    try:
        global pin_num,password_window
        
        print("your in password entry")
        password_window = Tk()
        password_window.title("account type window")
        password_window.geometry("800x760")
        
        label = Label(password_window, text = "please Enter your pin number", font = ("Arial Black",20))
        label.grid(row = 10, column = 10, padx = 100)
        
        pin_num = Entry(password_window, text = "pin here", font = ("Arial Black",20))
        pin_num.grid(row = 10, column = 12, padx = 100)
        
        submit_btn1 = Button(password_window, text = 'Submit',style = 'W.TButton',command = password_verify)
        submit_btn1.grid(row = 10, column = 14, padx = 100)
    
    except exception as err:
        
        print("password entry is not working ",err)
        sys.exit()
    


def account_type():
    print("your are in account window")
    #account_type = Tk()
    #account_type.title("account type window")
    #account_type.geometry("800x760")
    label = Label(English_window, text = "account type", font = ("Arial Black",20))
    label.grid(row = 5, column = 10, padx = 100)
    
    
    save_acc_btn = Button(English_window, text = ' Savings account',style = 'W.TButton',command = password_entry)
    save_acc_btn.grid(row = 6, column = 10, padx = 100)
    
    current_acc_btn = Button(English_window, text = 'Current account',style = 'W.TButton',command = password_entry)
    current_acc_btn.grid(row = 7, column = 10, padx = 100)
    
    password_entry()
    


def button1():
    print("your selected Telugu language")
    telugu_window = Tk()
    telugu_window.title("Telugu window")
    telugu_window.geometry("800x760")

    label = Label(telugu_window, text = "Telugu window", font = ("Arial Black",20))
    label.grid()
    
    #window1.destroy()
    telugu_window.mainloop()
    
    
def button2():
    print("your selected Hindi language")
    Hindi_window = Tk()
    Hindi_window.title("Hindi window")
    Hindi_window.geometry("800x760")

    label = Label(Hindi_window, text = "Hindi window", font = ("Arial Black",20))
    label.grid()
    
    Hindi_window.mainloop()
    
    
def button3():
    print("your selected English language")
    global English_window
    English_window = Tk()
    English_window.title("English window")
    English_window.geometry("800x760")

    # label = Label(English_window, text = "English window", font = ("Arial Black",20))
    # label.grid(row = 2, column = 10, padx = 100)
    
    account_type()
    
    #English_window.mainloop()
    
    
    
def submit_fun():
    global submit_btn1
    print("submit button pressed")
    card_num1 = card_num.get()
    print(card_num1)
    #checking the cardnumber is existing or not
    cursor1.execute("SELECT ATM_card_num FROM customers_data")
    for i in cursor1:
        print(i)
        card_exist =i
    
    print("enterd card num",type(card_num1))
    print("before exisiting card num",type(card_exist[0]))
    
    card_exist2 = str(card_exist[0])
    
    print("after exisiting card num",type(card_exist[0]))
    
    if card_exist2 == card_num1:
        print("your authorised user")
    
    
    
        #language selection
        language_sel = Tk()
        language_sel.title("English window")
        language_sel.geometry("800x760")
        
        
        # label = Label(window1, text = "Union Bank application", font = ("verdana",20))
        # label.grid()
        
        style = Style()
        
        # This will be adding style, and
        # naming that style variable as
        # W.Tbutton (TButton is used for ttk.Button).
        style.configure('W.TButton', font =	('calibri', 10, 'bold', 'underline'),foreground = 'red')
        
        # Style will be reflected only on
        # this button because we are providing
        # style only on this Button.
        ''' Button 1'''
        btn1 = Button(language_sel, text = 'Telugu',style = 'W.TButton',command = button1)
        btn1.grid(row = 2, column = 10, padx = 100)
        
        
        btn2 = Button(language_sel, text = 'Hindi',style = 'W.TButton',command = button2)
        btn2.grid(row = 3, column = 10, padx = 100)
        
        btn3 = Button(language_sel, text = 'English',style = 'W.TButton',command = button3)
        btn3.grid(row = 4, column = 10, padx = 100)
        
        
        
        btn4 = Button(language_sel, text = 'Quit',style = 'W.TButton',command = window1.destroy)
        btn4.grid(row = 5, column = 10, padx = 100)
        # Create text widget and specify size.
        
    else:
        print("card is not matching")
        



try:
        
    if __name__ == '__main__':
        
        window1 = Tk()
        # Code to add widgets will go here...
        window1.title("Union Bank")
        window1.geometry("800x760")
        
        style = Style()
        
        # This will be adding style, and
        # naming that style variable as
        # W.Tbutton (TButton is used for ttk.Button).
        style.configure('W.TButton', font =	('calibri', 10, 'bold', 'underline'),foreground = 'red')
        
        
        label = Label(window1, text = "Union Bank application", font = ("Arial Black",20))
        label.grid(row = 0, column = 10, padx = 100)
        
        
        
        label = Label(window1, text = "please type the card number", font = ("Arial Black",20))
        label.grid(row = 1, column = 10, padx = 100)
        
        card_num = Entry(window1, text = "please type the card number", font = ("Arial Black",20))
        card_num.grid(row = 1, column = 12, padx = 100)
        
        submit_btn1 = Button(window1, text = 'Submit',style = 'W.TButton',command = submit_fun)
        submit_btn1.grid(row = 1, column = 14, padx = 100)
        
    
        window1.mainloop()
        
        
except Exception as err:
    print("this is the error from main window",err)
    sys.exit()