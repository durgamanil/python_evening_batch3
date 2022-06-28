# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:42:45 2022

@author: durga
"""

#multiple inheritance

class a:
    def __init__(self):
        print("this is default constructor  aaaa")
           
class b:
    def __init__(self):
        print("this is default constructor  bbbb")
           
        
class c(b,a):
    def __init__(self):
        print("this is default constructor  cccc")
        b.__init__(self)
        a.__init__(self)
                 
c_obj = c()


################################
class father:
    def __init__(self):
        print("this is default constructor  father")
           
class mother:
    def __init__(self):
        print("this is default constructor mother")
           
        
class son(father,mother):
    def __init__(self):
        print("this is default constructor  son")
        mother.__init__(self)
        father.__init__(self)
                 
c_obj = son()



###methods of the multiple inheritance
class father:
    def __init__(self):
        print("this is default constructor  father")
        
    def father_house(self):
        print("this isthe father house")
           
class mother:
    def __init__(self):
        print("this is default constructor mother")
        
    def mother_house(self):
        print("this isthe mother house")
           
        
class son(father,mother):
    def __init__(self):
        print("this is default constructor  son")
        mother.__init__(self)
        father.__init__(self)
        
    
                 
c_obj = son()
c_obj.father_house()
c_obj.mother_house()


##############################
class father:
    def __init__(self):
        print("this is default constructor  father")
        
    def father_house(self):
        print("this isthe father house")
       
class mother:
    def __init__(self):
        print("this is default constructor mother")
        
    def mother_house(self):
        print("this isthe mother house")
               
class son(father,mother):
    def __init__(self):
        print("this is default constructor  son")
        mother.__init__(self)
        father.__init__(self)
        
    def display(self):
        self.father_house()
        self.mother_house()
        
c_obj = son()
c_obj.display()
#c_obj.father_house()
#c_obj.mother_house()







