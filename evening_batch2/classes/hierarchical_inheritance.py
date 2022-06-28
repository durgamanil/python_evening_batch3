# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:46:52 2022

@author: durga
"""

#heirarchical inheritance
syntax:
    class a:
        """statements"""
    class b(a):
        """statments"""
        
    class c(a):
        """statements"""
        
        
class a:
    """statements"""
    def __init__(self,aname):
        print("this is A class")
    
class b(a):
    """statments"""
    def __init__(self,bname,aname):
        print("this is b class")
        a.__init__(self,aname)
        
        
    
class c(a):
    """statements"""
    def __init__(self,cname,aname):
        self.cname = cname
        print("this is c class")
        a.__init__(self,aname)
    
    def display(self):
        print(self.cname)
        
        

c_object = c("radha","krishna")
b_obj = b("laxmi","vishnu")



#assignment
#class details:
    Name:
    id:
    fathername:
    mothername:
    address:
    company_name;
#employee:
#teacher/lawyer/doctor/engineer:




        
