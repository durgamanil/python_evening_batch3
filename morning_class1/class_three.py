# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 07:33:45 2022

@author: durga
"""

class vehicle():
    def __init__(self, model, name,engine_model):
        self.a = model
        self.b= name
        self.c = engine_model
        #pass
    
    def display(self):
        print(self.a)
        print(self.b)
        
        
    # def engine(self):
    #     print(self.a)
    #     print(self.b)
    #     print(self.c)
        
        
class car(vehicle):
    def __init__(self, model, name,engine_model):
        vehicle.__init__(self, model, name,engine_model)
      
    
    def display(self):
        #vehicle.display(self)
        print(self.a)
        print(self.b)
        print(self.c)
        

cl_obj = car("A100","Benz","esuze")
cl_obj.display()
print("*"*30)
#cl_obj.engine() 
#print(cl_obj.)
