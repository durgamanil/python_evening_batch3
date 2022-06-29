# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 07:02:10 2022

@author: durga
"""

# class my_class:
#     def __init__(self,name):
#         self.name = name
        
#     def display(self):
#         print("student name",self.name)

    

# a = my_class("srikanth")
# a.display()




# class my_class:
#     def __init__(self,name,rollno):
#         self.a = name
#         self.b = rollno
#         #pass
        
#     def display(self):
#         print("student name",self.a)
#         print("student rollno",self.b)

    

# a = my_class("srikanth","123")
# a.display()



class my_class:
    def __init__(self,name,rollno):
        self.a = name
        self.b = rollno
        #pass
        
    def display_name(self):
        print("student name",self.a)
         
    def display_rollno(self):
        print("student rollno",self.b)



student1 = my_class("kumar","12345")
student1.display_name()
student1.display_rollno()















