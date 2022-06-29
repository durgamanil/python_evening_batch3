# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 07:12:02 2022

@author: durga
"""

class vehicle():
    def __init__(self, model, name):
        self.model = model
        self.name = name
        
    # def display(self):
    #     print(self.model)
    #     print(self.name)print(self.name)
        
        
class car(vehicle):
    def __init__(self, model, name):
        vehicle.__init__(self, model, name)
        #pass
    
    def display(self):
        #vehicle.display(self)
        print(self.model)
        print(self.name)
        
        
class Bus(vehicle):
    def __init__(self, model, name):
        vehicle.__init__(self, model, name)
        
    

# cl_obj = vehicle("A100","Benz")
# cl_obj.display()  


car_obj = car("A100","Benz")
car_obj.display()  

# bus_obj = Bus("palle velugu","Tata")
# bus_obj.display()  










