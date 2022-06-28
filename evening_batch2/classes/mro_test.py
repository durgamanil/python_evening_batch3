# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:06:06 2022

@author: durga
"""

#multilevel inheritance

a-->b-->c

syntax:
    class a:
        """statements"""
    class b(a):
        """statements"""
    class c(b):
        """statements"""
  
        
  
class a:
    def __init__(self):
        print("this is default constructor for class A")
class b(a):
    """statements"""
    def __init__(self):
        print("this is default constructor for class b")
        a.__init__(self)
        
class c(b):
    """statements"""
    def __init__(self):
        b.__init__(self)
        print("this is default constructor for class c")
        
        
c_obj = c()



#accessing variables from different classes
class grandfather:
    def __init__(self,gfname):
        self.gfname = gfname
        print(self.gfname)
        
class father(grandfather):
    """statements"""
    def __init__(self,faname,gfname):
        # self.faname = faname
        # self.gfname = gfname
        # print(self.faname,self.gfname)
        grandfather.__init__(self,gfname)
        
           
class son(father):
    """statements"""
    def __init__(self,sname,faname,gfname):
        father.__init__(self,faname,gfname)
        # self.sname = sname
        # self.faname = faname
        # self.gfname = gfname
        
        # print(self.sname,self.faname,self.gfname)
        
c_obj = son("dhirubhai","mukesh","anil")



#methods to use in child class
class grandfather:
    def __init__(self,gfname):
        self.gfname = gfname
    
    def gfhouse(self):
        print("this is gf house")
        
class father(grandfather):
    """statements"""
    def __init__(self,faname,gfname):
        # self.faname = faname
        # self.gfname = gfname
        # print(self.faname,self.gfname)
        grandfather.__init__(self,gfname)
    
    def fatherhouse(self):
        print("this is father house")
        
           
class son(father):
    """statements"""
    def __init__(self,sname,faname,gfname):
        father.__init__(self,faname,gfname)
        # self.sname = sname
        # self.faname = faname
        # self.gfname = gfname
        
        # print(self.sname,self.faname,self.gfname)
        
    def son_house(self):
        print("this is son house")
        
s_obj = son("dhirubhai","mukesh","anil")
s_obj.son_house()
s_obj.fatherhouse()
s_obj.gfhouse()



d_obj = son("charanson","charan","chiru")
d_obj.son_house()
d_obj.fatherhouse()
d_obj.gfhouse()














    

        
        
    

