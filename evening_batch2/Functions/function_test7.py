# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 08:12:42 2022

@author: durga
"""

# def my_fn(100,b,c):
#     print("testing2")
#     print("a1--->",a)
#     print("b1--->",b)
#     print("c1--->",c)
#     d =a+b+c
#     print(d)
    

# a=200
# b=100
# c=300
# my_fn(a,b,c)





def my_fn(b,c,a):
    print("testing2")
    print("a1--->",a)#
    print("b1--->",b)
    print("c1--->",c)

    

name1=200
name2=100
name3=300
my_fn(name3,name2,name1)
print("after function call")


#monu---a=200,b=300,c=100
#naveen----b=300,a=200,c=100
#vandana---a=200 ,b=300 ,c=100





def my_fn(b,c,a):#(200,300,100)
    print("testing2")
    print("a--->",a)#
    print("b--->",b)
    print("c--->",c)

a=200
b=100
c=300
#my_fn(a,b,c)
#my_fn(c,b,a)#--->(300,100,200)
my_fn(a1,c1,b1)#---->(200,300,100)

#monu===>a=300,b=200,c=100

#naveen--->a=200,b=300,c=100
#meghana--->a =200,b=300,c=100


#a=100,b=200,c=300#sohan



# =============================================================================
# Default arguments
# =============================================================================

def my_fn(b1,c1,a=100):
    print("testing2")
    print("b--->",b1)
    print("c--->",c1)
    print("a--->",a)#


my_fn(100,200)





def my_fn(b1,c1,a=100):
    print("testing2")
    print("b--->",b1)
    print("c--->",c1)
    print("a--->",a)#


my_fn(100,200,300)


def greet_email(name,msg="happy sunday"):
    print("Hello\t"+name+"\t"+msg)
    
    
greet_email("naveen")
greet_email("Sohan","happy saturday")
greet_email("Mohan reddy")
greet_email("vandana")
greet_email("meghana")



#
def my_fn(b,c,a="a"):
    print("testing2")
    print("b--->",b)
    print("c--->",c)
    print("a--->",a)#


my_fn(100,200)

#a,b,c



def greet_email(name="customer",msg="happy sunday"):
    print("Hello\t"+name+"\t"+msg)
    
    
greet_email()
greet_email("Sohan","happy saturday")
greet_email("Mohan reddy")
greet_email(msg="happy monday")
greet_email("meghana")


# def my_fn(b,c,a):
#     print("testing2")
#     print("b--->",b)
#     print("c--->",c)
#     print("a--->",a)#


# my_fn(100,200)

def greet_email(msg="happy sunday",name="customer"):
    print("Hello\t"+name+"\t"+msg)
    
    
#greet_email()
greet_email("Sohan","happy saturday")
# greet_email("Mohan reddy")
greet_email(msg="happy monday",name="NTR")
# greet_email("meghana")







#interview question
l1 =[10,20,30]

def list_check(list1):
    print(list1)
    

list_check(l1)




def internet_availibility(ip_add,availble=True):
    print("connection at this ip add"+ip_add,availble)
    
internet_availibility("182.202.185.435",False)


# =============================================================================
# arbitrary arguments
# =============================================================================
def add(a,b,c):
    print(a+b+c)

# def add(a,b):
#     print(a+b)
    
# add(10,20)
#add(10,20,30)
add(10,20,30,40)



def add(a,b,c,d,e):
    #print(a+b+c+d+e)
    print(a,b,c,d,e)

# def add(a,b):
#     print(a+b)
    
add(10,20)
#add(10,20,30)
#add(10,20,30,40,50)


def meghana_add(*numbers):
    print(numbers)
    print(type(numbers))
    c =0
    for x in numbers:
        c = x+c  
    print(c)
    
    
#add(10,20)
#add(10,20,30)
meghana_add(10,20,30,40,50,60,50,60,30)


#pre-defined functions
#print
#len
#type
#id

#user_defined
meghana_add()
add()
my_fn
internet_availibility




def meghana_add(a,b,*numbers):
    print("a",a)
    print("b",b)
    print("numbers",numbers)

meghana_add(10,20,30,40,50,60,50,60,30)



# =============================================================================
# keyword arguments
# =============================================================================

# syntax:
#     def func_name(a,*name,**kwargs):
#         programming logic



def my_fun(**child):
    print(type(child))
    print("child name",child["first_name"],child["last_name"])
    
my_fun(first_name="konidela",last_name="ram charan")






# =============================================================================
# passing dictionary datatype arguments
# =============================================================================

def dict_fn(dict1):
    print(dict1)
    print(type(dict1))

my_dict ={"name":"TR",
       "surname":"N"}
dict_fn(my_dict)


# =============================================================================
# passing tuple datatype arguments
# =============================================================================

tuple1 = (1,2,3,4,56)

def tuple_fn(tuple1):
    print(tuple1)
    print(type(tuple1))
    
    
tuple_fn(tuple1)


# =============================================================================
# passing set arguments
# =============================================================================


set1 = {1,2,3,4,56}

def set_fn(set1):
    print(set1)
    print(type(set1))
    
    
set_fn(set1)


# =============================================================================
# return keyword
# =============================================================================


def add_fn(a,b):
    c = a+b
    return c



print(add_fn(10,20))



#interger type return
def add_fn(a,b):
    c = a+b
    return c



my_var = add_fn(10,20)#30

print(my_var)


#float type return

def add_fn(a,b):
    c = a+b
    return c



my_var = add_fn(10.9,20.5)#30

print(my_var)
print(type(my_var))


#string type return


def string_return_fn(str1):
    print("str",str1)
    return str1



str_var = string_return_fn("Raviteja")

print(str_var)
print(type(str_var))




















