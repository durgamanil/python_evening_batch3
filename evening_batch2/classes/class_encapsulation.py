# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:10:24 2022

@author: durga
"""

# =============================================================================
# Encapsulation
# =============================================================================


#we hiding/protecting the methods of one class to another class

class a:
    def method1(self):
        print("this is the method1")
        
    def method2(self):
        print("this is the method2")
        
        
class b:
    def method3(self):
        print("this is the method3")
        
    def method4(self):
        print("this is the method4")
    
    
    
c_obj = a()

c_obj.method1()
#c_obj.method3()
#c_obj.method4()

b_obj =b()
b_obj.method3()
b_obj.method4()





# =============================================================================
# 
# =============================================================================


def myfun():
    print("this is testing")
    print("i am learning python")
    print("mohan working the front end tech")
    
    
def myfun2():
    myfun()
    
    
def myfun3():
    myfun()
    
myfun2()
myfun3()




# =============================================================================
# 
# =============================================================================
class a:
    def method1(self):
        print("this is the method1")
        
    def method2(self):
        print("this is the method2")
        
        
class b:
    def method3(self):
        print("this is the method3")
        
    def method4(self):
        print("this is the method4")
        
        a_obj  = a()
        a_obj.method1()
        a_obj.method2()
        
        # method1()
        # method2()
    
    


b_obj =b()
b_obj.method3()
b_obj.method4()

# =============================================================================
# 
# =============================================================================

class a:
    def method1(self):
        print("this is the method1")
        
    def method2(self):
        print("this is the method2")
        
      
a_obj  = a()

class b:
    def method3(self):
        print("this is the method3")
        
    def method4(self):
        print("this is the method4")
        
        
        a_obj.method1()
        a_obj.method2()


b_obj =b()
b_obj.method3()
b_obj.method4()





