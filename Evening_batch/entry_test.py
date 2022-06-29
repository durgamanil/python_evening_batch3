




from  tkinter import * 
#from tkinter import tk
import tkinter as tk


    
def home_ui():
    width =600
    height = 800
    window = Tk()
    window.geometry("800x600")
    label1 = tk.Label(window,text="first name").pack()
    a = tk.Entry(window)
    a.pack()
    a1=a.get()
    
    B = Button(window, text = "OK")
    B.pack(anchor = S)
    print(a1)
    

    window.mainloop()
    
    
    
    

if __name__ == '__main__':
    home_ui()
    
    
    
    
    
    
    
    
    
    
    
    
    
    