# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 08:06:51 2022

@author: durga
"""

def student_names( name1 ):
    print("name1---->",name1)
    
    
   
student_names("chakri") 


#function call should be below the function defination
student_names("chakri") 
def student_names( name1 ):
    print("name1---->",name1)
    
    
    
#multiple functions

def student_marks(marks):
    print(marks)

def student_names( name1 ):
    print("name1---->",name1)
    
student_names("chakri") 
student_marks(100)
   


def student_marks(marks):
    print(marks)

def student_names( name1 ):
    print("name1---->",name1)

student_marks(100)
student_names("chakri") 


def student_marks(marks):
    print(marks)
    
    
student_marks(100)

def student_names( name1 ):
    print("name1---->",name1)


student_names("chakri") 



#list---arguments

def student_marks(marks):
    print(marks)
    print(marks[0])
    print(marks[1])
    print(marks[2])
    print(marks[3])
    print(marks[4])
    print(marks[5])
    

def student_names( name1 ):
    print("name1---->",name1)

list2 = [100,85,95,96,95]
student_names("chakri") 
student_marks(list2)


def student_marks(marks):
    print(marks)
    for i in marks:
        print(i)
    

def student_names( name1 ):
    print("name1---->",name1)

list2 = [100,85,95,96,95]
student_names("chakri") 
student_marks(list2)


#tuple arguments


def student_marks(marks):
    print(marks)
    for i in marks:
        print(i)
    

def student_names( name1 ):
    print("name1---->",name1)

tuple1= (100,85,95,96,95)
student_names("chakri") 
student_marks(tuple1)


def student_marks(marks):
    print(marks)

def student_names( name1 ):
    print("name1---->",name1)

names_marks = {"student_name1":"chakri",
               "student1_marks":98,
               "student2_name":"sharath",
               "student2_marks":97}
student_names("chakri") 
student_marks(names_marks)

#set arguments


def student_marks(marks):
    print(marks)
    print(type(marks))
    

def student_names( name1 ):
    print("name1---->",name1)

names_marks = {"student_name1","chakri",
               "student1_marks",98,
               "student2_name","sharath",
               "student2_marks",97}
student_names("chakri") 
student_marks(names_marks)



# return keyword
#it will return the values
#return ---single values
#reurn ----multiple values


def addition(a,b):
    print(a,b)
    c = a+b
    return c

sum1 = addition(10,20)
print("sum1==>",sum1)



def addition(a,b):
    print(a,b)
    d =  40
    c = a+b+d
    return c

sum1 = addition(10,20)
print("sum1==>",sum1)


def addition(a,b):
    print(a,b)
    d =  40
    c = a+b+d
    return 100

sum1 = addition(10,20)
print("sum1==>",sum1)



def addition(a,b):
    print(a,b)
    d =  40
    c = a+b+d
    return "bahubali"

sum1 = addition(10,20)
print("sum1==>",sum1)


def check_return(a,b):
    print(a,b)
    
    c = "Hello"+ a + b 
    return c

return_output = check_return("good morning", "mohan")
print(return_output)



#multiple_return values

def return_multiple_values(a,b):
    print(a,b)
    sum1 = a+b
    sub1 = b - a
    return sum1,sub1

returned_val = return_multiple_values(10,20)
print(returned_val)


def return_multiple_values(a,b):
    print(a,b)
    sum1 = a+b
    sub1 = b - a
    return sum1,sub1

sum2,sub2 = return_multiple_values(10,20)
print(sum2)
print(sub2)


#pass the values
def return_multiple_values(a,b):
    print(a,b)
    sum1 = a+b
    sub1 = b - a
    return sum1,sub1

sum2,sub2 = return_multiple_values(10,20)
print(sum2)
print(sub2)


def return_multiple_values(a,b):
    print(a,b)
    sum1 = a+b
    sub1 = b - a
    return sum1,sub1


c = 100
d = 40
sum2,sub2 = return_multiple_values(c,d)
print(sum2)
print(sub2)


#doc string
#documentation string


def return_multiple_values(a,b):
    """this is the function takes two arguments integer type
        it will return the multiple values"""    
    print(a,b)
    sum1 = a+b
    sub1 = b - a
    return sum1,sub1


c = 100
d = 40
sum2,sub2 = return_multiple_values(c,d)
print(sum2)
print(sub2)

print(return_multiple_values.__doc__)

#single quotes

def return_multiple_values(a,b):
    '''this is the function takes two arguments integer type
        it will return the multiple values'''
      
    print(a,b)
    sum1 = a+b
    sub1 = b - a
    
    return sum1,sub1

c = 100
d = 40
sum2,sub2 = return_multiple_values(c,d)
print(sum2)
print(sub2)

print(return_multiple_values.__doc__)




#comments
def return_multiple_values(a,b):
      
    print(a,b)
    sum1 = a+b
    sub1 = b - a
    """this is the function takes two arguments integer type
        it will return the multiple values"""  
    return sum1,sub1


c = 100
d = 40
sum2,sub2 = return_multiple_values(c,d)
print(sum2)
print(sub2)

print(return_multiple_values.__doc__)







