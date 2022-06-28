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
    table_exist = cursor1.execute("CREATE TABLE teacher_table ( sno int,\
                        teacher_name varchar(255) ,\
                        teacher_admission_number int,\
                        teacher_gender varchar(255) ,\
                        teacher_father varchar(255) ,\
                        teacher_mother varchar(255) ,\
                        teacher_dob  varchar(255) ,\
                        teacher_standard int,\
                        teacher_contact varchar(255) ,\
                        teacher_doa varchar(255) ,\
                        teacher_section int,\
                        teacher_address varchar(255)) ")
    print(table_exist)
    
except:
    print("teacher table already exist")
    
    
def show_table():
    conn = pymysql.connect(host='localhost',user='root',password = "",db='school_management')
    cursor1 = conn.cursor()
    cursor1.execute("SELECT * FROM `teacher_table`")
    #print(cursor1)
    #print(cursor1.fetchall())
    records = cursor1.fetchall()
    #print(records)
    
    
def delete():
    conn = pymysql.connect(host='localhost',user='root',password = "",db='school_management')
    cursor1 = conn.cursor()
    
    tables = cursor1.execute("DELETE FROM `teacher_table` WHERE 1")
    print(tables)
    
    for selected_item in teacher_table.selection():
        item = teacher_table.item(selected_item)['values']
        selected_item = teacher_table.selection()[0]
        teacher_table.delete(selected_item)
    
def clear_entries():
    teacher_name_entry.delete(0,END)
    teacher_admission_number_entry.delete(0,END)
    teacher_gender_entry.delete(0,END)
    teacher_email_entry.delete(0,END)
    teacher_father_entry.delete(0,END)
    teacher_mother_entry.delete(0,END)
    teacher_dob_entry.delete(0,END)
    teacher_standard_entry.delete(0,END)
    teacher_contact_entry.delete(0,END)
    teacher_doa_entry.delete(0,END)
    teacher_section_entry.delete(0,END)
    teacher_address_entry.delete(0,END)
 


def teacher_add():
    teacher_name_text  = 0
    teacher_admission_number_text = 0
    teacher_gender_text =0 
    teacher_email_text = 0
    teacher_father_text = 0
    teacher_mother_text = 0
    teacher_dob_text = 0
    teacher_standard_text =0
    teacher_contact_text = 0
    teacher_doa_text = 0
    teacher_section_text = 0
    teacher_address_text = 0
    
    # if(teacher_name_entry.get() == '' or teacher_admission_number_entry.get() ==''
    #    or teacher_gender_entry.get() =='' or teacher_email_entry.get() =='' or teacher_father_entry.get() == '' 
    #    or teacher_mother_entry.get() == '' or teacher_dob_entry.get() ==''
    #    or teacher_standard_entry.get() == '' or teacher_contact_entry.get() == ''
    #    or teacher_doa_entry.get() == '' or teacher_section_entry.get() == ''
    #    or teacher_address_entry.get() == ''):
    #     messagebox.showerror("required fields","please enter all the fields")
            
    teacher_name_text               = teacher_name_entry.get()
    teacher_admission_number_text   = teacher_admission_number_entry.get()
    teacher_gender_text             = teacher_gender_entry.get() 
    teacher_email_text              = teacher_email_entry.get()
    teacher_father_text             = teacher_father_entry.get() 
    teacher_mother_text             = teacher_mother_entry.get()
    teacher_dob_text                = teacher_dob_entry.get()
    teacher_standard_text           = teacher_standard_entry.get()
    teacher_contact_text            = teacher_contact_entry.get()
    teacher_doa_text                =   teacher_doa_entry.get()
    teacher_section_text            =   teacher_section_entry.get()
    teacher_address_text            = teacher_address_entry.get()
    
    print(teacher_name_text)
    print(teacher_admission_number_text ,teacher_gender_text ,teacher_father_text )
    print(teacher_mother_text ,teacher_dob_text ,teacher_standard_text )
    print(teacher_contact_text ,teacher_doa_text ,teacher_section_text )
    print(teacher_address_text)
    
    sql = "INSERT INTO `teacher_table`(`sno`, `teacher_name`, `teacher_admission_number`, `teacher_gender`, `teacher_father`, `teacher_mother`, `teacher_dob`, `teacher_standard`, `teacher_contact`, `teacher_doa`, `teacher_section`, `teacher_address`) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = ('3',teacher_name_text, teacher_admission_number_text,teacher_gender_text,teacher_father_text,teacher_mother_text ,teacher_dob_text,teacher_standard_text,teacher_contact_text,teacher_doa_text,teacher_section_text,teacher_address_text)
    
    cursor1.execute(sql, val)
    
    conn.commit()
    print("commit is done")
    print("cursor reached here")
        
    
    #return 
    value = (teacher_name_text,teacher_admission_number_text,
                         teacher_gender_text,teacher_email_text ,
                         teacher_father_text ,teacher_mother_text,
                         teacher_dob_text,teacher_standard_text,
                         teacher_contact_text,teacher_doa_text,
                         teacher_section_text,teacher_address_text) 
    
    teacher_table.insert('',END,values= value)
    clear_entries()
    
        
        
#def teacher_register_fn():
st_reg_win = Tk()
st_reg_win.title("school management system")
st_reg_win.geometry("1200x800")

#header block
heading_frame =Frame(st_reg_win)
heading_frame.place(x =0,y=0,width =1200,height=60)

header = Label(heading_frame,text="teacher registration form",bg="#00bfff",fg="white",font=("arial",20))
header.pack(side=TOP,fill=X)

#teacher entry block
#st_entry_fr = Frame(st_reg_win,padx =20,bg ="red")
st_entry_fr = Frame(st_reg_win,padx =20)
st_entry_fr.place(x=40,y=80,width =1200,height=300)

#teacher_name
teacher_name = Label(st_entry_fr,text="teacher Name")
teacher_name.grid(row =1,column =1,padx = 20, pady = 6)

#admission number
teacher_admission =  Label(st_entry_fr,text=" Admission Number")
teacher_admission .grid(row =2,column =1,padx = 20, pady = 6)

#gender
teacher_gender = Label(st_entry_fr,text="Gender")
teacher_gender.grid(row =3,column =1,padx = 20, pady = 6)
#email id
teacher_email = Label(st_entry_fr,text="Email")
teacher_email.grid(row =4,column =1,padx = 20, pady = 6)
#father name
teacher_father_name = Label(st_entry_fr,text="Father Name")
teacher_father_name.grid(row =1,column =3,padx = 20, pady = 6)
#mother name
teacher_mother_name = Label(st_entry_fr,text="Mother Name")
teacher_mother_name.grid(row =2,column =3,padx = 20, pady = 6)
#DOB
teacher_dob = Label(st_entry_fr,text="Date of birth")
teacher_dob .grid(row =3,column =3,padx = 20, pady = 6)
#standard/class
teacher_standard = Label(st_entry_fr,text="standard")
teacher_standard.grid(row =4,column =3,padx = 20, pady = 6)
#contact number
teacher_contact = Label(st_entry_fr,text="Contact number")
teacher_contact.grid(row =1,column =5,padx = 20, pady = 6)
#Date of admission
teacher_doa = Label(st_entry_fr,text="Date of Admission")
teacher_doa.grid(row =2,column =5,padx = 20, pady = 6)
#section
teacher_section = Label(st_entry_fr,text="section")
teacher_section.grid(row =3,column =5,padx = 20, pady = 6)
#address
teacher_address = Label(st_entry_fr,text="Address")
teacher_address.grid(row =4,column =5,padx = 20, pady = 6)



#variables for stroing entries
teacher_name_value         = StringVar()
teacher_admission_value    = IntVar()
teacher_gender_value       = StringVar()
teacher_email_value        = StringVar()
teacher_father_name_value  =    StringVar()
teacher_mother_name_value  =    StringVar()
teacher_dob_val            =    IntVar()
teacher_standard_value     =    IntVar()
teacher_contact_value      =    IntVar()
teacher_doa_value          =    IntVar()
teacher_section_value      =    StringVar()
teacher_address_value      =    StringVar()



#entries entry block
teacher_name_entry = Entry(st_entry_fr,textvariable=teacher_name_value,width =30)
teacher_name_entry.grid(row =1,column =2)

#admission number
teacher_admission_number_entry = Entry(st_entry_fr,textvariable=teacher_admission_value ,width =30)
teacher_admission_number_entry.grid(row =2,column =2)


#gender
teacher_gender_entry = Entry(st_entry_fr,textvariable=teacher_gender_value,width =30)
teacher_gender_entry.grid(row =3,column =2)
#email id
teacher_email_entry = Entry(st_entry_fr,textvariable=teacher_email_value,width =30)
teacher_email_entry.grid(row =4,column =2)
#father name
teacher_father_entry = Entry(st_entry_fr,textvariable=teacher_father_name_value,width =30)
teacher_father_entry.grid(row =1,column =4)
#mother name
teacher_mother_entry = Entry(st_entry_fr,textvariable=teacher_mother_name_value,width =30)
teacher_mother_entry.grid(row =2,column =4)
#DOB
teacher_dob_entry = Entry(st_entry_fr,textvariable=teacher_dob_val,width =30)
teacher_dob_entry.grid(row =3,column =4)
#standard/class
teacher_standard_entry = Entry(st_entry_fr,textvariable=teacher_standard_value,width =30)
teacher_standard_entry.grid(row =4,column =4)
#contact number
teacher_contact_entry = Entry(st_entry_fr,textvariable=teacher_contact_value,width =30)
teacher_contact_entry.grid(row =1,column =6)
#Date of admission
teacher_doa_entry = Entry(st_entry_fr,textvariable=teacher_doa_value,width =30)
teacher_doa_entry.grid(row =2,column =6)
#section
teacher_section_entry = Entry(st_entry_fr,textvariable=teacher_section_value,width =30)
teacher_section_entry.grid(row =3,column =6)
#address
teacher_address_entry = Entry(st_entry_fr,textvariable=teacher_address_value,width =30)
teacher_address_entry.grid(row =4,column =6)


#Button(st_entry_fr,text="submit",command=teacher_add).grid(row=5,column=2)


app2 = Frame(st_reg_win, padx=10)
app2.place(x=100, y=290, width=710, height=100)

#Button & packing it and assigning it a command
Button(app2, text="ADD", command=teacher_add, bg="#E6E6FA", pady=3, padx=40).grid(row=5, column=1, padx=20)
Button(app2, text="DELETE", command=delete, bg="#E6E6FA", pady=3, padx=30).grid(row=5, column=2, padx=10)
Button(app2, text="EXIT", command=st_reg_win.destroy, bg="#E6E6FA", pady=3, padx=30).grid(row=5, column=3,padx=20)

# Search Teacher's
search = Label(app2, text="Search teacher's")
search.grid(row=5, column=4, pady=6, padx=15)
searchvalue = StringVar()

searchentry = Entry(app2, textvariable=searchvalue, width=30)
searchentry.grid(row=5, column=5)


#view of the teachers
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

columns = ("teacher_name","teacher_admission_no","teacher_gender",
               "teacher_email","teacher_father_name","teacher_mother_name",
               "teacher_dob","teacher_standard","teacher_contact_no",
               "teacher_doa","teacher_section","teacher_address" )

teacher_table = ttk.Treeview(view_frame,style="Custom.Treeview",columns=columns,
                             show = "headings",
                             xscrollcommand=xscroll.set,
                             yscrollcommand=yscroll.set)

#setting scrollbar from two side x, y directions
yscroll.config(command=teacher_table.yview)
xscroll.config(command= teacher_table.xview)

yscroll.pack(side=RIGHT,fill=Y)
xscroll.pack(side=BOTTOM,fill=X)


#headings
teacher_table.heading("teacher_name",text = "teacher name")
teacher_table.heading("teacher_admission_no",text = "teacher_admission_no")
teacher_table.heading("teacher_gender",text = "teacher_gender")
teacher_table.heading("teacher_email",text = "teacher_email")
teacher_table.heading("teacher_father_name",text = "teacher_father_name")
teacher_table.heading("teacher_mother_name",text = "teacher_mother_name")
teacher_table.heading("teacher_dob",text = "teacher_dob")
teacher_table.heading("teacher_standard",text = "teacher_standard")
teacher_table.heading("teacher_contact_no",text = "teacher_contact_no")
teacher_table.heading("teacher_doa",text = "teacher_doa")
teacher_table.heading("teacher_section",text = "teacher_section")
teacher_table.heading("teacher_address",text = "teacher_address")


#columns
teacher_table.column("teacher_name", width=80)
teacher_table.column("teacher_admission_no", width=100,anchor=CENTER)
teacher_table.column("teacher_gender", width=150,anchor= CENTER)
teacher_table.column("teacher_email", width=150,anchor= CENTER)
teacher_table.column("teacher_father_name", width=120,anchor= CENTER)
teacher_table.column("teacher_mother_name", width=100,anchor= CENTER)
teacher_table.column("teacher_dob", width=100,anchor= CENTER)
teacher_table.column("teacher_standard", width=100,anchor= CENTER)
teacher_table.column("teacher_contact_no", width=100,anchor= CENTER)
teacher_table.column("teacher_doa", width=100,anchor= CENTER)
teacher_table.column("teacher_section", width=100,anchor= CENTER)
teacher_table.column("teacher_address", width=100,anchor= CENTER)

teacher_table.pack(fill=BOTH,expand=TRUE)
show_table()

st_reg_win.mainloop()



