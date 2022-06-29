# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 08:18:20 2022

@author: durga
"""

# =============================================================================
# dictionary topic session 2
# pop method
# =============================================================================
#pop method will remove the item with specified key
dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":2022} 
print(dict3)
dict3.pop("bike")
print(dict3)


#popitem method
#the last key and value will be removed

dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":2022} 
print(dict3)
dict3.popitem()
print(dict3)

#del keyword

dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":2022} 
print(dict3)
del dict3
print(dict3)

dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":2022} 

for item in dict3:
    print(item)

for item in dict3:
    print(dict3[item])
    
for i in dict3.keys():
    print(i)

for i in dict3.values():
    print(i)
    
for i,j in dict3.items():
    print(i,"---->",j)

a = {}
print(type(a))

    
#nesting the dictionary

student = {"student1":{"name":"kumar",
                       "roll_no":1234,
                       "admissionyear":2022
                        },
           "student2":{
                         "name":"ramesh",
                         "roll_no":1235,
                         "admissionyear":2022},
           "student3":{
                   "name":"mukesh",
                   "roll_no":1236,
                   "admissionyear":2022}
           }
print(student)


#fetching the details

#print(student["student1"])
print(student["student1"]["name"])

print(student["student1"]["roll_no"])

print(student["student1"]["admissionyear"])



print(student["student2"]["name"])

print(student["student2"]["roll_no"])

print(student["student2"]["admissionyear"])




dict3 ={"company":"Hero",
        "bike":"glomour",
        "year":2022} 
print(dict3)

var1 = dict3.setdefault("bike","pulsar")

print(var1)
print(dict3)












