


from  tkinter import * 
#from tkinter import tk
import tkinter as tk



def submit_fun():
    a1 = a.get()
    print(a1)
    
    
def check_in():
    global a1,a
    text1 = "Welcome come to Check IN"
    window2 = Tk()
    window2.geometry("700x500")
    print("enter user details")
    label2 = tk.Label(window2,text=text1,padx=0,pady=20).grid(column=500, row=0)
    label2 = tk.Label(window2,text="dfksfjklsdgjfkljfdkjksjfjgsdjf",padx=0,pady=20).grid(column=500, row=1)
    label2 = tk.Label(window2,text="Wkldjfkjadfjdskjf",padx=0,pady=20).grid(column=500, row=2)
    label2 = tk.Label(window2,text="dksjfklsdjfkjaskfds",padx=0,pady=20).grid(column=500, row=3)
    label2 = tk.Label(window2,text="dskfjksdjfksjdkfjkdsjf",padx=0,pady=20).grid(column=500, row=4)
    a = tk.Entry(window2)
    a.grid(column=500,row=6)
    a1 = a.get()
    
    
    tk.Button(window2, text="Submit" ,command= submit_fun).grid(column=800, row=150)
    tk.Button(window2, text="Quit" ,command= window2.destroy).grid(column=900, row=100)
    
    
def check_out():
    window3 = Tk()
    window3.geometry("700x500")
    print("enter user details")
    label2 = tk.Label(window3,text="Welcome come to Check OUT",padx=0,pady=20)
    label2.grid(column=5000, row=0)
    tk.Button(window3, text="Quit" ,command= window3.destroy).grid(column=900, row=100)
    
def room_information():
    window4 = Tk()
    window4.geometry("700x500")
    print("enter user details")
    label2 = tk.Label(window4,text="Welcome come to room info",padx=0,pady=20)
    label2.grid(column=5000, row=0)
    tk.Button(window4, text="Quit" ,command= window4.destroy).grid(column=900, row=100)   
    
def guest_availability():
    window5 = Tk()
    window5.geometry("700x500")
    print("enter user details")
    label2 = tk.Label(window5,text="Welcome come to guest availability",padx=0,pady=20)
    label2.grid(column=5000, row=0)
    tk.Button(window5, text="Quit" ,command= window5.destroy).grid(column=900, row=100)  
    

def empty_room_info():
    window6 = Tk()
    window6.geometry("700x500")
    print("enter user details")
    label2 = tk.Label(window6,text="Welcome come to empty room info",padx=0,pady=20)
    label2.grid(column=5000, row=0)
    tk.Button(window6, text="Quit" ,command= window6.destroy).grid(column=900, row=100)  
    
    
    
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
    
    
 
    label2 = tk.Label(window,text="Taj Banjara",padx=0,pady=20)
    label2.grid(column=5000, row=0)
    
    
    tk.Button(window, text="Check IN" ,command= check_in).grid(column=100, row=100)
    tk.Button(window, text="Check OUT",command= check_out).grid(column=500, row=100)
    tk.Button(window, text="Room Info",command= room_information ).grid(column=600, row=100)
    tk.Button(window, text="Guest Availability",command= guest_availability).grid(column=700, row=100)
    tk.Button(window, text="Empty room",command= empty_room_info).grid(column=800, row=100)
    
    
    tk.Button(window, text="Quit" ,command= window.destroy).grid(column=900, row=100)
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    