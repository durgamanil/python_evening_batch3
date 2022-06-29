# # -*- coding: utf-8 -*-
# """
# Created on Sat Mar  5 06:46:24 2022

# @author: durga
# """

# #multiple inheritance
# class  mother():
#     def __init__(self):
#         #self.first_name = fname
#         #self.last_name = lname
#         pass
    
#     def mother_salary(self):
#         print("salary 10,000,000")
    
#     def mother_house(self):
#         print("mother house")
        
# class father():
#     def __init__(self):
#         #grandfather.__init__(self, fname)
#         pass
        
#     def father_salary(self):
#         print("salary-50,000,000")
        
#     def father_house(self):
#         print("father house")
              
# class child(father,mother):
#     def __init__(self,fname):
#         mother.__init__(self)
#         father.__init__(self)
#         #pass 
#     def child_business(self):
#         print("jewellary shop")
     
# x = child("ramcharan")
# #print(type(x))
# x.mother_salary()
# x.mother_house()
# x.father_salary()
# x.father_house()
# x.child_business()


# #multiple inheritance
# class  mother():
#     def __init__(self):
#         #self.first_name = fname
#         #self.last_name = lname
#         pass
    
#     def mother_salary(self):
#         print("salary 10,000,000")
    
#     def house(self):
#         print("mother house")
        
# class father():
#     def __init__(self):
#         #grandfather.__init__(self, fname)
#         pass
        
#     def father_salary(self):
#         print("salary-50,000,000")
        
#     def house(self):
#         print("father house")
              
# class child(father,mother):
#     def __init__(self,fname):
#         mother.__init__(self)
#         father.__init__(self)
#         #pass
        
#     def child_business(self):
#         print("jewellary shop")
     
# x = child("ramcharan")
# #print(type(x))
# x.mother_salary()
# x.house()
# x.father_salary()
# x.house()





# #multiple inheritance
# class  mother():
#     def __init__(self):
#         #self.first_name = fname
#         #self.last_name = lname
#         pass
    
#     def mother_salary(self):
#         print("salary 10,000,000")
    
#     def house(self):
#         print("mother house")
        
# class father():
#     def __init__(self):
#         #grandfather.__init__(self, fname)
#         pass
        
#     def father_salary(self):
#         print("salary-50,000,000")
        
#     def house(self):
#         print("father house")
        
        
# class brother():
#     def __init__(self):
#         #grandfather.__init__(self, fname)
#         pass
        
#     def brother_salary(self):
#         print("salary-50,000,000")
        
#     def house(self):
#         print("brother house")
              
# class child(brother,mother,father):
#     def __init__(self,fname):
#         mother.__init__(self)
#         father.__init__(self)
#         brother.__init__(self)
#         #pass

#     def child_business(self):
#         print("jewellary shop")
     
# x = child("ramcharan")
# #print(type(x))
# x.mother_salary()
# x.house()
# x.father_salary()
# x.house()
# x.brother_salary()
# x.house()

#o/p
# salary 10,000,000
# mother house
# salary-50,000,000
# mother house
# salary-50,000,000
# mother house


class Calculation1:  
    def Summation(self,a,b):  
        return a+b; 
    
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
    
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
    
    
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  








