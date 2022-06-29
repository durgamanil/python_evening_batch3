# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 07:55:36 2022

@author: durga
"""

class Employee:
    def __init__(self,name,rollno):
        self.a = name
        self.b = rollno

        
    def display_name(self):
        print("employee name",self.a)
         
    def display_idno(self):
        print("employee rollno",self.b)


empl_names = ["kumar","sandeep","srikanth","uday"]


for i in empl_names:
    emp1 = Employee(i, 1234)
    emp1.display_name()
    emp1.display_idno()
    print("="*30)

