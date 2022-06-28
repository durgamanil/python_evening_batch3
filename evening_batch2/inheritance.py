# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 07:06:21 2022

@author: durga
"""

# class  person():
#     def __init__(self, fname, lname):
#         self.first_name = fname
#         self.last_name = lname
    
#     def display(self):
#         print(self.first_name,self.last_name)
        

# class student(person):
#     def __init__(self,fname,lname):
#         person.__init__(self, fname, lname)
    
# x = person("srikanth","nagula")
# x.display()



# class  person():
#     def __init__(self, fname, lname):
#         self.first_name = fname
#         self.last_name = lname
    
#     def display(self):
#         print(self.first_name,self.last_name)
        

# class student(person):
#     def __init__(self,fname,lname):
#         person.__init__(self, fname, lname)
    
    

    
# x = student("srikanth","nagula")
# x.display()


# class  father():
#     def __init__(self, fname):
#         self.first_name = fname
#         #self.last_name = lname
    
#     def display(self):
#         print(self.first_name)
    
#     def myhouse(self):
#         print("this is father house")
        

# class child(father):
#     def __init__(self,fname):
#         father.__init__(self, fname)
#         #pass
    
    
# x = father("srikanth")
# x.display() 
# x.myhouse() 
    
# x = child("kumar")
# x.display()
# x.myhouse()



# class  father():
#     def __init__(self, fname):
#         self.first_name = fname
#         #self.last_name = lname
    
#     def display(self):
#         print(self.first_name)
    
#     def myhouse(self):
#         print("this is father house")
        

# class child(father):
#     def __init__(self,fname):
#         father.__init__(self, fname)
        
#     def child_salary(self):
#         print("10000000")
        
        
    
    
# # x = father("srikanth")
# # x.display() 
# # x.myhouse() 
    
# x = child("kumar")
# x.display()
# x.myhouse()
# x.child_salary()






# class  father():
#     def __init__(self, fname):
#         self.first_name = fname
#         #self.last_name = lname
    
#     def display(self):
#         print(self.first_name)
    
#     def myhouse(self):
#         print("this is father house")
        

# class child(father):
#     def __init__(self,fname):
#         father.__init__(self, fname)
        
#     def child_salary(self):
#         print("10000000")
        
        
    
    
# x = father("srikanth")
# x.display() 
# x.myhouse()
# x.child_salary() #not allowed
    
# x = child("kumar")
# x.display()
# x.myhouse()
# x.child_salary()



# #multileve inheritance
# class  grandfather():
#     def __init__(self, fname):
#         self.first_name = fname
#         #self.last_name = lname
    
#     def display(self):
#         print(self.first_name)
    
#     def myhouse(self):
#         print("this is grand father house")
        
# class father(grandfather):
#     def __init__(self,fname):
#         grandfather.__init__(self, fname)
              
# class child(father):
#     def __init__(self,fname):
#         father.__init__(self, fname)
        
    
# # x = father("srikanth")
# # x.display() 
# # x.myhouse()
# # x.child_salary() #not allowed
    
# x = child("kumar")
# x.display()
# x.myhouse()



#multileve inheritance
# class  grandfather():
#     def __init__(self, fname):
#         self.first_name = fname
#         #self.last_name = lname
    
#     def display(self):
#         print(self.first_name)
    
#     def myhouse(self):
#         print("this is grand father house")
        
# class father(grandfather):
#     def __init__(self,fname):
#         grandfather.__init__(self, fname)
        
#     def father_salary(self):
#         print("salary-50,000,000")
        
#     def father_house(self):
#         print("father house")
              
# class child(father):
#     def __init__(self,fname):
#         father.__init__(self, fname)
        
#     def child_business(self):
#         print("jewellary shop")
        
    
# # x = father("srikanth")
# # x.display() 
# # x.myhouse()
# # x.father_salary() #not allowed

    
# x = child("ramcharan")
# x.display()
# x.myhouse()
# x.father_house()
# x.father_salary()
# x.child_business()




#multileve inheritance
class  grandfather():
    def __init__(self, fname):
        self.first_name = fname
        #self.last_name = lname
    
    def display(self):
        print(self.first_name)
    
    def myhouse(self):
        print("this is grand father house")
        
class father(grandfather):
    def __init__(self,fname):
        grandfather.__init__(self, fname)
        
    def father_salary(self):
        print("salary-50,000,000")
        
    def father_house(self):
        print("father house")
              
class child(father):
    def __init__(self,fname):
        father.__init__(self, fname)
        
    def child_business(self):
        print("jewellary shop")
 

y =grandfather("NTR")
y.child_business()# not allowed
    
x = father("srikanth")
x.display() 
x.myhouse()
x.father_salary() #not allowed
x.child_business() # not allowed

    
x = child("ramcharan")
#print(type(x))
x.display()
x.myhouse()
x.father_house()
x.father_salary()
x.child_business()



