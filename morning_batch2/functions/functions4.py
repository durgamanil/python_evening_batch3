# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 08:06:52 2022

@author: durga
"""

def student_names(name):
    print(name)
    
student_names("sharath")


def student_names(name1,name2):
    print(name1,name2)
    
student_names("sharath","manoj")  

def student_names(name1,name2,name3):
    print(name1,name2,name3)
    
student_names("sharath","manoj","chakri")  

#arbitrary arguments
syntax:
    *args


def student_names(*name1):
    print(name1)
    
student_names("sharath","manoj","chakri")  




def student_names(*name1):
    print(name1[0])
    print(name1[1])
    print(name1[2])
    
student_names("sharath","manoj","chakri")  

def student_names(*name1):
    print("hello " + name1[0])
    print(name1[1])
    print(name1[2])
    
student_names("sharath","manoj","chakri") 

def student_names(*name1):
    print(name1)
    print("hello " + name1[0])
    print(name1[1])
    print(name1[2])
    
student_names("sharath","manoj","chakri","rana","prabhas","mahesh") 


def student_names(name2,name3, *name1):
    print(name2)
    print(name3)
    print(name1)

    
student_names("sharath","manoj","chakri","rana","prabhas","mahesh") 


def student_names(*name1,name2,name3):
    print(name2)
    print(name3)
    print(name1)

    
student_names("sharath","manoj","chakri","rana","prabhas","mahesh") 


def student_names(name2="sharath",name3="manoj", *rem_names):
    print(name2)
    print(name3)
    print(rem_names)

    
student_names("chakri","rana","prabhas","mahesh") 


# =============================================================================
# keyword arguments
# =============================================================================

syntax:
    **keyword args
    **kwargs
    

def student_names( **rem_names):
    print(rem_names)
    print(rem_names["name1"])

    
student_names(name1 = "chakri",name2 ="rana",name3="prabhas",name4= "mahesh") 




def student_names( name1,name2 ,*args ,**rem_names):
    print("name1---->",name1)
    print("name2---->",name2)
    print("args------",args)
    print(rem_names)
    

    
student_names("chakri","rana","chiru","mukesh",name3="prabhas",name4= "mahesh") 


#order

def student_names( *args ,**rem_names,name1,name2 ):
    print("name1---->",name1)
    print("name2---->",name2)
    print("args------",args)
    print(rem_names)
    

    
student_names("chakri","rana","chiru","mukesh",name3="prabhas",name4= "mahesh") 


def student_names( **rem_names,name1,name2 ,*args ):
    print("name1---->",name1)
    print("name2---->",name2)
    print("args------",args)
    print(rem_names)
    

    
student_names("chakri","rana","chiru","mukesh",name3="prabhas",name4= "mahesh") 


















