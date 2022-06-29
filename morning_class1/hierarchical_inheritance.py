# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 07:22:19 2022

@author: durga
"""
# =============================================================================
# hierarchical inheritance
# =============================================================================

        
class father():
    def __init__(self):
        #grandfather.__init__(self, fname)
        pass
        
    def father_salary(self):
        print("salary-50,000,000")
        
    def house(self):
        print("father house")
        
        
class  mother(father):
    def __init__(self):
        father.__init__(self)
              
class child(father):
    def __init__(self,fname):
        father.__init__(self)

    def child_business(self):
        print("jewellary shop")
     
x = child("ramcharan")
x.father_salary()
x.house()
print("*"*30)
y = mother()
y.father_salary()
y.house()







