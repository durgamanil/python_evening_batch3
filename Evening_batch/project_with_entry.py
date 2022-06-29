


from  tkinter import * 
#from tkinter import tk
import tkinter as tk
import os





def room_information():
    button = 1
    if button == 1:
        window4 = Tk()
        window4.geometry("700x500")
        label3 = tk.Label(window4,text= "this is single bedroom ",padx=0,pady=20).grid(column=500, row=2)
    elif button ==2:
        window4 = Tk()
        window4.geometry("700x500")
        label3 = tk.Label(window4,text= "this is single bedroom ",padx=0,pady=20).grid(column=500, row=2)
    elif button ==3:
        window4 = Tk()
        window4.geometry("700x500")
        label3 = tk.Label(window4,text= "this is single bedroom ",padx=0,pady=20).grid(column=500, row=2)
    elif button ==4:
        window4 = Tk()
        window4.geometry("700x500")
        label3 = tk.Label(window4,text= "this is single bedroom ",padx=0,pady=20).grid(column=500, row=2)
    elif button ==5:
        window4 = Tk()
        window4.geometry("700x500")
        label3 = tk.Label(window4,text= "this is single bedroom ",padx=0,pady=20).grid(column=500, row=2)
    elif button ==6:
        window4 = Tk()
        window4.geometry("700x500")
        label3 = tk.Label(window4,text= "this is single bedroom ",padx=0,pady=20).grid(column=500, row=2)
        
    
    
    

def submit_fun():
    global first_name1,address1,mbl_no1,aadhar_no1
    first_name1 = first_name.get()
    address1 = address.get()
    mbl_no1 = mbl_no.get()
    aadhar_no1 = aadhar_no.get()
    #print(a.get(),"\n",b.get(),"\n",c.get())
    print(first_name1,"\n",address1,"\n",mbl_no1,"\n",aadhar_no1)
    #details stored in files
    #details_file = open("customer_details.txt",'r')
    details_file = open("customer_details.txt",'a')
    details_file.write(first_name1)
    details_file.write(address1)
    details_file.write(mbl_no1)
    details_file.write(aadhar_no1)

        
    
    
def check_in():
    global first_name,address,mbl_no,aadhar_no
    text1 = "Welcome come to Check IN"
    window2 = Tk()
    window2.geometry("700x500")
    #print("enter user details")
    label2 = tk.Label(window2,text=text1,padx=0,pady=20).grid(column=500, row=0)
    label3 = tk.Label(window2,text= "Full Name",padx=0,pady=20).grid(column=500, row=1)
    
    first_name = tk.Entry(window2)
    first_name.grid(column=600,row=1)
    
    label4 = tk.Label(window2,text= "Address",padx=0,pady=20).grid(column=500, row=2)
    
    address = tk.Entry(window2)
    address.grid(column=600,row=2)
    
    label5 = tk.Label(window2,text= "Mobile Number",padx=0,pady=20).grid(column=500, row=3)
    
    mbl_no = tk.Entry(window2)
    mbl_no.grid(column=600,row=3)
    
    label5 = tk.Label(window2,text= "Aadhar card Number",padx=0,pady=20).grid(column=500, row=4)
    
    aadhar_no = tk.Entry(window2)
    aadhar_no.grid(column=600,row=4)

    tk.Button(window2, text="Submit" ,command= submit_fun).grid(column=800, row=8)
    tk.Button(window2, text="Quit" ,command= window2.destroy).grid(column=900, row=8)
    
    
def check_out():
    window3 = Tk()
    window3.geometry("700x500")
    print("enter user details")
    label2 = tk.Label(window3,text="Welcome come to Check OUT",padx=0,pady=20)
    label2.grid(column=5000, row=0)
    tk.Button(window3, text="Quit" ,command= window3.destroy).grid(column=900, row=100)
    
def rooms():
    window4 = Tk()
    window4.geometry("700x500")
    #print("enter user details")
    label2 = tk.Label(window4,text="Welcome come to room info",padx=0,pady=20)
    label2.grid(column=5000, row=0)
    #tk.Button(window4, text="100" ,command= room_information,height = 5,width =20).grid(column=800, row=1)  
    tk.Button(window4, text="100" ,command= room_information,height = 5,width =20).grid(column=800, row=1)
    tk.Button(window4, text="101" ,command= room_information,height = 5,width =20).grid(column=900, row=1)   
    tk.Button(window4, text="102" ,command= room_information,height = 5,width =20).grid(column=800, row=2)   
    tk.Button(window4, text="103" ,command= room_information,height = 5,width =20).grid(column=900, row=2)   
    tk.Button(window4, text="104" ,command= room_information,height = 5,width =20).grid(column=800, row=3) 
    tk.Button(window4, text="105" ,command= room_information,height = 5,width =20).grid(column=900, row=3) 
    tk.Button(window4, text="Quit" ,command= window4.destroy,height = 5,width =30).grid(column=900, row=7)  
    
    
    
def guest_availability():
    window5 = Tk()
    window5.geometry("700x500")
    #print("enter user details")
    label2 = tk.Label(window5,text="Welcome come to guest availability",padx=0,pady=20)
    label2.grid(column=5000, row=0)
    #print(first_name1)
    details_file = open("customer_details.txt",'r')
    #print(details_file.read())
    label2 = tk.Label(window5,text=details_file.read(),padx=0,pady=20)
    label2.grid(column=5000, row=1)
    
    # details_file = open("customer_details.txt",'r')
    # print(details_file.read())
    
    
    tk.Button(window5, text="Quit" ,command= window5.destroy).grid(column=900, row=100)  
    
    

def empty_room_info():
    details_file = open("customer_details.txt",'r')
    print(details_file.read())
    root = Tk()
    
    # specify size of window.
    root.geometry("250x170")
    
    # Create text widget and specify size.
    T = Text(root, height = 5, width = 52)
    
    # Create label
    l = Label(root, text = "Fact of the Day")
    l.config(font =("Courier", 14))
    
    Fact = """room are empty
    100th room is empty
    101 room is not empty
    102 room is empty"""
    
    
    
    # Create an Exit button.
    b2 = Button(root, text = "Exit",command = root.destroy)
    
    l.pack()
    T.pack()
   
    b2.pack()
    
    # Insert The Fact.
    T.insert(tk.END, Fact)
    
    tk.mainloop()

    
    #text_area = tk.Text(window6)
    text_area = tk.text(window6)
    # tk.Button(window6, text="Quit" ,command= window6.destroy).grid(column=900, row=100)  
    
    
    
def home_ui():
    width =600
    height = 800
    # for i in range(0,10):
    window = Tk()
    #window2 = Tk()
    window.geometry("1000x600")
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
    
    label2 = tk.Label(window,text="Taj Banjara",font=("Arial", 25))
    label2.grid(column=500, row=0)
    
    
    tk.Button(window, text="Check IN" ,command= check_in,height = 5,width =30).grid(column=900, row=1)
    tk.Button(window, text="Check OUT",command= check_out,height = 5,width =30).grid(column=900, row=5)
    tk.Button(window, text="Room Info",command= rooms,height = 5,width =30 ).grid(column=900, row=8)
    tk.Button(window, text="Guest Availability",command= guest_availability,height = 5,width =30).grid(column=900, row=10)
    tk.Button(window, text="Empty room",command= empty_room_info,height = 5,width =30).grid(column=900, row=12)
    
    tk.Button(window, text="Quit" ,command= window.destroy,height = 5,width =30).grid(column=900, row=13)
    
   
    window.mainloop()
    #window2.mainloo()
    
    
if __name__ == '__main__':
    
    Room_numbers =[100,101,102,103,104,105]
    
    if not(os.path.isfile("customer_details.txt")):
        #print(details_file.read())
        details_file = open("customer_details.txt",'x')
    
    home_ui()
    
    
    
    
    
    
    
    
    
    
    
    
    
    