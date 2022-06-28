# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:05:05 2022

@author: durga
"""

b = 3000

class mycls():
    a = 10
    print(b)
    
class myclass2():
    d =5000
    print(b)
    
    
class myclass3():
    def __init__(self):
        print("this is default constructor")
    

a1 = mycls()
print(a1.a)

b2 = myclass2()
print(b2.d)

mc3 = myclass3()

#inheritances
1.single inheritance


class a:
    def __init__(self):
        print("this is default constructor  aaaa")
        
class b(a):
    def __init__(self):
        a.__init__(self)
        print("this is defalut constructor bbb")
        
        
a1 =b()



###############this is about default constructor

class a:
    def __init__(self):
        print("this is default constructor  aaaa")
        
class b(a):
    def __init__(self):
        print("this is defalut constructor bbb")
        a.__init__(self)
        
        
        
a1 =b()



# single inheritance methods

class engine:
    def __init__(self):
        print("this is default constructor  engine")
        
    def engine_model(self):
        print("esuzi")
        
    
        
class car(engine):
    def __init__(self):
        print("this is defalut constructor car")
        engine.__init__(self)
        
    def car_brand(self):
        print("TATA")
        
    def car_door(self):
        print("open close the doors")
        
        
        
car_obj = car()

car_obj.car_brand()
car_obj.car_door()
car_obj.engine_model()




###################################
class car:
    def __init__(self):
        print("this is default constructor  engine")
        
    def engine_model(self):
        print("esuzi")
        
    
        
class engine(car):
    def __init__(self):
        print("this is defalut constructor car")
        car.__init__(self)
        
    def car_brand(self):
        print("TATA")
        
    def car_door(self):
        print("open close the doors")
        
        
        
engine_obj = engine()





class a:
    def __init__(self):
        print("this is default constructor  aaaa")
        
        
class b(a):
    def __init__(self):
        print("this is default constructor  bbbb")
        a.__init__(self)
        
        
class c(a):
    def __init__(self):
        print("this is default constructor  cccc")
        a.__init__(self)
        
        
        
c_obj = c()
b_obj = b()



    
    








    




