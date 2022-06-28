# -*- coding: utf-8 -*-
"""
Created on Fri May  6 19:10:54 2022

@author: durga
"""

class Employee:
    #this is method
    def __init__(self,name,serial_no,company):
        self.name = name
        self.serial_no = serial_no
        self.company =company
        
    def display(self):
        print(self.name)
        print(self.serial_no)
        print(self.company)
        
    def test(self):
        print("this is yet another method")
        
        
a1 = Employee("sohan",20,"Google")
a1.display()
#a1.test()



#
class Employee:
    #this is method
    def __init__(self,name,serial_no,company):
        self.a = name
        self.b = serial_no
        self.c =company
        
    def display(self):
        print(self.a)
        print(self.b)
        print(self.c)
        
    def test(self):
        print("this is yet another method")
        
        
a1 = Employee("sohan",20,"Google")
a1.display()





class Employee:
    #this is method
    def __init__(self,name,serial_no,company):
        self.a = name
        self.b = serial_no
        self.c =company
        
    def display(self):
        print(self.a)
        print(self.b)
        print(self.c)
        
    def test(self):
        print("this is yet another method")
        
        
a1 = Employee("sohan",20,"Google")
a1.display()



# def myfun1(a,b,c):
#     num1= a
#     num2 =b
#     num3 =c
#     print(num1,num2,num3)
      
# def myfun2():
#     print(num1,num2,num3)
    
    
# myfun1(10,20,30)
# myfun2()



class Employee:
    #this is method
    def __init__(self,name,serial_no,company):
        self.a = serial_no
        self.b = company
        self.c =name
        
    def display(self):
        print(self.a)
        print(self.b)
        print(self.c)
        
    def test(self):
        print("this is yet another method")
        
        
a1 = Employee("sohan",20,"Google")
a1.display()




# =============================================================================
# return value and class object
# =============================================================================
class fun2():
    pass

def fun(a):
    print("inside fun--a",a)
    #return a

var = fun(10)
print("var", var)
m1 = fun2()
print(type(m1))


# =============================================================================
# 
# =============================================================================

class fun2:
    pass

n1= fun2()
print(n1)
print(type(fun2))

#list

# list1 = [1,2,3,4]
# print(type(list1))


# =============================================================================
# methods in the classes
# =============================================================================

class calculator:
    #this is method
    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
 
    def display(self):
        print(self.a)
        print(self.b)
        print(type(self.a))
        print(type(self.b))        
        
    def addition(self):
        print(self.a + self.b)
        
        
    def substraction(self):
        print(self.a - self.b)
        
    def multiplication(self):
        print(self.a * self.b)
        
        
a1 = calculator(20000,10000)

a1.display()
a1.addition()
a1.substraction()
a1.multiplication()






# =============================================================================
# 
# =============================================================================
class calculator:
    #this is method
    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
 
    def display(self):
        print(self.a)
        print(self.b)
        print(type(self.a))
        print(type(self.b))        
        
    def addition(self):
        print(self.a + self.b)
        
        
    def substraction(self):
        print(self.a - self.b)
        
    def multiplication(self):
        print(self.a * self.b)
        
        
a1 = calculator(20000,10000)
a1.addition(),a1.substraction(),a1.multiplication()

#greet the person
# good morning
# good afternooon
# goood evening
# good night


# =============================================================================
# 
# =============================================================================

class calculator:
    #this is method
    s = 1000
    c = 2000
    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
 
    def display(self):
        print(self.a)
        print(self.b)
        
a1 = calculator(20000,10000)
a1.display()#
print("="*30)
a1.a = 50000
a1.b = 10000000
a1.display()



# =============================================================================
# pass keyword in classes and methods
# =============================================================================

class calculator:
    pass
        
a1 = calculator()




class calculator:

    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
 
    def display(self):
        pass
    def mytest(self):
        print("this is mytest method")
        
a1 = calculator(20000,10000)
a1.display()
a1.mytest()

# =============================================================================
# deleting the class
# =============================================================================

class calculator:

    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
 
    def display(self):
        pass
    def mytest(self):
        print("this is mytest method")
        
a1 = calculator(20000,10000)
del a1

# print(a1)














