from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import pymysql


# conn = pymysql.connect(host='localhost',user='root',password = "",db='school_management')
# cursor1 = conn.cursor()
# print(cursor1)


try :
    mydb = pymysql.connect( host="localhost",  user="root",  password="")
    mycursor = mydb.cursor()
    a = mycursor.execute("CREATE DATABASE school_management")
    if a ==1:
        print("database created successfully")
except:
    print("database already exists")


# =============================================================================
# creating tables
# =============================================================================
try:
    conn = pymysql.connect(host='localhost',user='root',password = "",db='school_management')
    cursor1 = conn.cursor()
    table_exist = cursor1.execute("CREATE TABLE employee_table ( sno int,\
                        employee_name varchar(255) ,\
                        employee_admission_number int,\
                        employee_gender varchar(255) ,\
                        employee_father varchar(255) ,\
                        employee_mother varchar(255) ,\
                        employee_dob  varchar(255) ,\
                        employee_standard int,\
                        employee_contact varchar(255) ,\
                        employee_doa varchar(255) ,\
                        employee_section int,\
                        employee_address varchar(255)) ")
    print(table_exist)
    
except:
    print("employee table already exist")
    
    
def show_table():
    conn = pymysql.connect(host='localhost',user='root',password = "",db='school_management')
    cursor1 = conn.cursor()
    cursor1.execute("SELECT * FROM `employee_table`")
    #print(cursor1)
    #print(cursor1.fetchall())
    records = cursor1.fetchall()
    #print(records)
    
    
def delete():
    conn = pymysql.connect(host='localhost',user='root',password = "",db='school_management')
    cursor1 = conn.cursor()
    
    tables = cursor1.execute("DELETE FROM `employee_table` WHERE 1")
    print(tables)
    
    for selected_item in employee_table.selection():
        item = employee_table.item(selected_item)['values']
        selected_item = employee_table.selection()[0]
        employee_table.delete(selected_item)
    
def clear_entries():
    employee_name_entry.delete(0,END)
    employee_admission_number_entry.delete(0,END)
    employee_gender_entry.delete(0,END)
    employee_email_entry.delete(0,END)
    employee_father_entry.delete(0,END)
    employee_mother_entry.delete(0,END)
    employee_dob_entry.delete(0,END)
    employee_standard_entry.delete(0,END)
    employee_contact_entry.delete(0,END)
    employee_doa_entry.delete(0,END)
    employee_section_entry.delete(0,END)
    employee_address_entry.delete(0,END)
 


def employee_add():
    employee_name_text  = 0
    employee_admission_number_text = 0
    employee_gender_text =0 
    employee_email_text = 0
    employee_father_text = 0
    employee_mother_text = 0
    employee_dob_text = 0
    employee_standard_text =0
    employee_contact_text = 0
    employee_doa_text = 0
    employee_section_text = 0
    employee_address_text = 0
    
    # if(employee_name_entry.get() == '' or employee_admission_number_entry.get() ==''
    #    or employee_gender_entry.get() =='' or employee_email_entry.get() =='' or employee_father_entry.get() == '' 
    #    or employee_mother_entry.get() == '' or employee_dob_entry.get() ==''
    #    or employee_standard_entry.get() == '' or employee_contact_entry.get() == ''
    #    or employee_doa_entry.get() == '' or employee_section_entry.get() == ''
    #    or employee_address_entry.get() == ''):
    #     messagebox.showerror("required fields","please enter all the fields")
            
    employee_name_text               = employee_name_entry.get()
    employee_admission_number_text   = employee_admission_number_entry.get()
    employee_gender_text             = employee_gender_entry.get() 
    employee_email_text              = employee_email_entry.get()
    employee_father_text             = employee_father_entry.get() 
    employee_mother_text             = employee_mother_entry.get()
    employee_dob_text                = employee_dob_entry.get()
    employee_standard_text           = employee_standard_entry.get()
    employee_contact_text            = employee_contact_entry.get()
    employee_doa_text                =   employee_doa_entry.get()
    employee_section_text            =   employee_section_entry.get()
    employee_address_text            = employee_address_entry.get()
    
    print(employee_name_text)
    print(employee_admission_number_text ,employee_gender_text ,employee_father_text )
    print(employee_mother_text ,employee_dob_text ,employee_standard_text )
    print(employee_contact_text ,employee_doa_text ,employee_section_text )
    print(employee_address_text)
    
    sql = "INSERT INTO `employee_table`(`sno`, `employee_name`, `employee_admission_number`, `employee_gender`, `employee_father`, `employee_mother`, `employee_dob`, `employee_standard`, `employee_contact`, `employee_doa`, `employee_section`, `employee_address`) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = ('3',employee_name_text, employee_admission_number_text,employee_gender_text,employee_father_text,employee_mother_text ,employee_dob_text,employee_standard_text,employee_contact_text,employee_doa_text,employee_section_text,employee_address_text)
    
    cursor1.execute(sql, val)
    
    conn.commit()
    print("commit is done")
    print("cursor reached here")
        
    
    #return 
    value = (employee_name_text,employee_admission_number_text,
                         employee_gender_text,employee_email_text ,
                         employee_father_text ,employee_mother_text,
                         employee_dob_text,employee_standard_text,
                         employee_contact_text,employee_doa_text,
                         employee_section_text,employee_address_text) 
    
    employee_table.insert('',END,values= value)
    clear_entries()
    
        
        
#def employee_register_fn():
st_reg_win = Tk()
st_reg_win.title("school management system")
st_reg_win.geometry("1200x800")

#header block
heading_frame =Frame(st_reg_win)
heading_frame.place(x =0,y=0,width =1200,height=60)

header = Label(heading_frame,text="employee registration form",bg="#00bfff",fg="white",font=("arial",20))
header.pack(side=TOP,fill=X)

#employee entry block
#st_entry_fr = Frame(st_reg_win,padx =20,bg ="red")
st_entry_fr = Frame(st_reg_win,padx =20)
st_entry_fr.place(x=40,y=80,width =1200,height=300)

#employee_name
employee_name = Label(st_entry_fr,text="employee Name")
employee_name.grid(row =1,column =1,padx = 20, pady = 6)

#admission number
employee_admission =  Label(st_entry_fr,text=" Admission Number")
employee_admission .grid(row =2,column =1,padx = 20, pady = 6)

#gender
employee_gender = Label(st_entry_fr,text="Gender")
employee_gender.grid(row =3,column =1,padx = 20, pady = 6)
#email id
employee_email = Label(st_entry_fr,text="Email")
employee_email.grid(row =4,column =1,padx = 20, pady = 6)
#father name
employee_father_name = Label(st_entry_fr,text="Father Name")
employee_father_name.grid(row =1,column =3,padx = 20, pady = 6)
#mother name
employee_mother_name = Label(st_entry_fr,text="Mother Name")
employee_mother_name.grid(row =2,column =3,padx = 20, pady = 6)
#DOB
employee_dob = Label(st_entry_fr,text="Date of birth")
employee_dob .grid(row =3,column =3,padx = 20, pady = 6)
#standard/class
employee_standard = Label(st_entry_fr,text="standard")
employee_standard.grid(row =4,column =3,padx = 20, pady = 6)
#contact number
employee_contact = Label(st_entry_fr,text="Contact number")
employee_contact.grid(row =1,column =5,padx = 20, pady = 6)
#Date of admission
employee_doa = Label(st_entry_fr,text="Date of Admission")
employee_doa.grid(row =2,column =5,padx = 20, pady = 6)
#section
employee_section = Label(st_entry_fr,text="section")
employee_section.grid(row =3,column =5,padx = 20, pady = 6)
#address
employee_address = Label(st_entry_fr,text="Address")
employee_address.grid(row =4,column =5,padx = 20, pady = 6)



#variables for stroing entries
employee_name_value         = StringVar()
employee_admission_value    = IntVar()
employee_gender_value       = StringVar()
employee_email_value        = StringVar()
employee_father_name_value  =    StringVar()
employee_mother_name_value  =    StringVar()
employee_dob_val            =    IntVar()
employee_standard_value     =    IntVar()
employee_contact_value      =    IntVar()
employee_doa_value          =    IntVar()
employee_section_value      =    StringVar()
employee_address_value      =    StringVar()



#entries entry block
employee_name_entry = Entry(st_entry_fr,textvariable=employee_name_value,width =30)
employee_name_entry.grid(row =1,column =2)

#admission number
employee_admission_number_entry = Entry(st_entry_fr,textvariable=employee_admission_value ,width =30)
employee_admission_number_entry.grid(row =2,column =2)


#gender
employee_gender_entry = Entry(st_entry_fr,textvariable=employee_gender_value,width =30)
employee_gender_entry.grid(row =3,column =2)
#email id
employee_email_entry = Entry(st_entry_fr,textvariable=employee_email_value,width =30)
employee_email_entry.grid(row =4,column =2)
#father name
employee_father_entry = Entry(st_entry_fr,textvariable=employee_father_name_value,width =30)
employee_father_entry.grid(row =1,column =4)
#mother name
employee_mother_entry = Entry(st_entry_fr,textvariable=employee_mother_name_value,width =30)
employee_mother_entry.grid(row =2,column =4)
#DOB
employee_dob_entry = Entry(st_entry_fr,textvariable=employee_dob_val,width =30)
employee_dob_entry.grid(row =3,column =4)
#standard/class
employee_standard_entry = Entry(st_entry_fr,textvariable=employee_standard_value,width =30)
employee_standard_entry.grid(row =4,column =4)
#contact number
employee_contact_entry = Entry(st_entry_fr,textvariable=employee_contact_value,width =30)
employee_contact_entry.grid(row =1,column =6)
#Date of admission
employee_doa_entry = Entry(st_entry_fr,textvariable=employee_doa_value,width =30)
employee_doa_entry.grid(row =2,column =6)
#section
employee_section_entry = Entry(st_entry_fr,textvariable=employee_section_value,width =30)
employee_section_entry.grid(row =3,column =6)
#address
employee_address_entry = Entry(st_entry_fr,textvariable=employee_address_value,width =30)
employee_address_entry.grid(row =4,column =6)


#Button(st_entry_fr,text="submit",command=employee_add).grid(row=5,column=2)


app2 = Frame(st_reg_win, padx=10)
app2.place(x=100, y=290, width=710, height=100)

#Button & packing it and assigning it a command
Button(app2, text="ADD", command=employee_add, bg="#E6E6FA", pady=3, padx=40).grid(row=5, column=1, padx=20)
Button(app2, text="DELETE", command=delete, bg="#E6E6FA", pady=3, padx=30).grid(row=5, column=2, padx=10)
Button(app2, text="EXIT", command=st_reg_win.destroy, bg="#E6E6FA", pady=3, padx=30).grid(row=5, column=3,padx=20)

# Search Teacher's
search = Label(app2, text="Search employee's")
search.grid(row=5, column=4, pady=6, padx=15)
searchvalue = StringVar()

searchentry = Entry(app2, textvariable=searchvalue, width=30)
searchentry.grid(row=5, column=5)


#view of the employees
view_frame= Frame(st_reg_win,bg ="red", bd=2, relief=RIDGE)
view_frame.place(x=20,y=350,width =1200,height=400)

#tree view
#view_fram_in = ttk.Treeview(view_frame)

style = ttk.Style()
style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.image", {'side': 'right'}),  # , 'sticky': ''
            ("Custom.Treeheading.text", {'sticky': 'we'})
        ]})
    ]}),
])

style.configure("Custom.Treeview.Heading", background="lightgrey", foreground="black", relief="groove")
style.map("Custom.Treeview.Heading", relief=[('active', 'flat'), ('pressed', 'sunken')])

xscroll = Scrollbar(view_frame,orient=HORIZONTAL)
yscroll = Scrollbar(view_frame,orient = VERTICAL)

columns = ("employee_name","employee_admission_no","employee_gender",
               "employee_email","employee_father_name","employee_mother_name",
               "employee_dob","employee_standard","employee_contact_no",
               "employee_doa","employee_section","employee_address" )

employee_table = ttk.Treeview(view_frame,style="Custom.Treeview",columns=columns,
                             show = "headings",
                             xscrollcommand=xscroll.set,
                             yscrollcommand=yscroll.set)

#setting scrollbar from two side x, y directions
yscroll.config(command=employee_table.yview)
xscroll.config(command= employee_table.xview)

yscroll.pack(side=RIGHT,fill=Y)
xscroll.pack(side=BOTTOM,fill=X)


#headings
employee_table.heading("employee_name",text = "employee name")
employee_table.heading("employee_admission_no",text = "employee_admission_no")
employee_table.heading("employee_gender",text = "employee_gender")
employee_table.heading("employee_email",text = "employee_email")
employee_table.heading("employee_father_name",text = "employee_father_name")
employee_table.heading("employee_mother_name",text = "employee_mother_name")
employee_table.heading("employee_dob",text = "employee_dob")
employee_table.heading("employee_standard",text = "employee_standard")
employee_table.heading("employee_contact_no",text = "employee_contact_no")
employee_table.heading("employee_doa",text = "employee_doa")
employee_table.heading("employee_section",text = "employee_section")
employee_table.heading("employee_address",text = "employee_address")


#columns
employee_table.column("employee_name", width=80)
employee_table.column("employee_admission_no", width=100,anchor=CENTER)
employee_table.column("employee_gender", width=150,anchor= CENTER)
employee_table.column("employee_email", width=150,anchor= CENTER)
employee_table.column("employee_father_name", width=120,anchor= CENTER)
employee_table.column("employee_mother_name", width=100,anchor= CENTER)
employee_table.column("employee_dob", width=100,anchor= CENTER)
employee_table.column("employee_standard", width=100,anchor= CENTER)
employee_table.column("employee_contact_no", width=100,anchor= CENTER)
employee_table.column("employee_doa", width=100,anchor= CENTER)
employee_table.column("employee_section", width=100,anchor= CENTER)
employee_table.column("employee_address", width=100,anchor= CENTER)

employee_table.pack(fill=BOTH,expand=TRUE)
show_table()

st_reg_win.mainloop()



