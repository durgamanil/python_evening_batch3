# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 08:17:37 2022

@author: durga
"""

# =============================================================================
# Dictionary
#dict--keyword, constructor
# =============================================================================
in dictionary will store the values using 
key and values pairs
syntax:
    {key:value,
    key1:value1}
    
ex1:
    
dict1 ={"fruit1":"apple",
        "fruit2":"mango",
        "fruit3":"banana"}

print(dict1)

print(type(dict1))

#len---function
print(len(dict1))

#ex2

dict2 ={1:"apple",
        2:"mango",
        3:"banana"}

print(dict2)

#accessing the key and values
print(dict2[1])#not indexes...these are keys
print(dict2[2])
print(dict2[3])

#different datatypes

dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":1996}

print(dict3["company"])
print(dict3["bike"])
print(dict3["year"])


#key and values should be there otherwise it will syntax error
dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":}

print(dict3["company"])
print(dict3["bike"])
print(dict3["year"])

dict3 ={"company":"Hero",
        "bike":"glomour",
        :1996}

print(dict3["company"])
print(dict3["bike"])
print(dict3["year"])


#list and tuples format for the values is allowed
dict4 = {"fruits":["mango","orange","lemon","popaya"],
         "flowers":("rose","lilli","lotus"),
         "inventedyear":1995,
         "date":15
         }

print(dict4)

print(dict4["fruits"])
print(type(dict4["fruits"]))
print(type(dict4["flowers"]))

#by using index method , 
#you can get the individual elements from the list
print(dict4)
print(dict4["fruits"][0])
print(dict4["fruits"][1])
print(dict4["fruits"][2])
print(dict4["fruits"][3])

print(dict4["flowers"][0])
print(dict4["flowers"][1])
print(dict4["flowers"][2])

#updating the values
dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":1996}

print(dict3)
dict3["company"]="Honda"
print(dict3)

#methods of the dictionary
dir(dict3)
['__class__', '__class_getitem__',
 '__contains__', '__delattr__',
 '__delitem__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__ior__', '__iter__',
 '__le__', '__len__', '__lt__', '__ne__',
 '__new__', '__or__',
 '__reduce__', '__reduce_ex__',
 '__repr__', '__reversed__',
 '__ror__', '__setattr__',
 '__setitem__', '__sizeof__',
 '__str__', '__subclasshook__',
 'clear',
 'copy',
 'fromkeys',
 'get',
 'items',
 'keys',
 'pop',
 'popitem',
 'setdefault',
 'update',
 'values']


#keys methods
dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":1996}

print(dict3.keys())

#if we want to collect in one variable we can do that
keys1 =  dict3.keys()
print(keys1)

for i in keys1:
    print(i)
    
#values methods

dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":1996}

print(dict3.values())

dict3["year"] = 2022
print(dict3)

#extra key on same key name

dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":1996,
        "year":2022} 

print(dict3["year"])
print(dict3)



#'items', method in tuple format it will print

print(dict3.items())


#dict3 add extra key and values
dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":2022} 
print(dict3)
dict3["developer"]="anil"

print(dict3)

#'clear', remove the keys and values from the dictionary

dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":2022} 

print(dict3)
dict3.clear()
print(dict3)


#'copy', method

dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":2022} 

#print(dict3)

dict4 = dict3.copy()
print("dict3",dict3)
print("dict4",dict4)
print(id(dict3))
print(id(dict4))

dict5 = dict3
print(id(dict5))
print(id(dict3))

#update method

dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":2022} 
print(dict3)
dict3.update({"released":2023})
print(dict3)


