# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 07:34:36 2022

@author: durga
"""

#dictionary is adavanced datatype in the python

"""
syntax:
    
 dict1 =   {"key1":"value1",
     "key2":"value2"
     
     }
 
"""
 
 
 
 
#example1:
     
    
#string type dictionary

     
dict1 =   {
    "fruit1":"apple",
     "fruit2":"value2"
     
     }


print(dict1)

print(type(dict1))


print(dict1["fruit1"])




#int type dictionary
dict1 =   {
        1:"apple",
        2:"banana",
        3:"orange"
     
     }


print(dict1)

print(type(dict1))

print(dict1[1])
#checking the keys
dict1.keys()

#checking the values
dict1.values()

print(id(dict1))


#int  type values dictionary
dict1 =   {
        1:45,
        2:76,
        3:95
     
     }

print(dict1)

print(type(dict1))

print(dict1[2])
#checking the keys
print(dict1.keys())

#checking the values
print(dict1.values())

print(id(dict1))


#mixed type


dict1 =   {
        
        "name":"Naveen",
        "rno":123456,
        "marks":455.6,
        "passRfail":True #true stands for pass      
     
     }

print(dict1["name"])
print(dict1["rno"])
print(dict1["marks"])
print(dict1["passRfail"])


a = str(dict1["rno"])

print(type(dict1["name"]))
print(type(dict1["rno"]))
print(type(dict1["marks"]))
print(type(dict1["passRfail"]))
print(a, type(a))


#list in dictionary

list1= [1,2,3,4,5]
print(type(list1))

print(list1)


dict2 = {
    "fruits":["orange","mango","banana"],
    "flowers":["lilli","rose","jasmine"],
    "wines":["vodka","TeacherC","lawyerc","EngineerC"]    
    }

#print(dict2)

print(dict2["wines"])
#print(dict2)

print(dict2.keys())


#tuple in the dictionary
dict2 = {
    "fruits":("orange","mango","banana"),
    "flowers":("lilli","rose","jasmine"),
    "wines":("vodka","TeacherC","lawyerc","EngineerC")   
    }


print(dict2["wines"])
print(dict2.keys())
print(dict2.values())


#nested

dir(dict2)

['__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__ior__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__ne__',
 '__new__',
 '__or__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__ror__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
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



dict3 = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(dict3)


"""
python keywords	
and	 exec	finally	assert
break	class	for	continue
def	del	elif	else
except	from	global	if
import	in	is	lambda
not	or	pass	print
raise	return	try	while
with	return	yield:
 """   
    
print(type({1: 'Geeks', 2: 'For', 3:'Geeks'}))

a = "100"
b = float(a)

c = str(b)

print(a,"\n",b,c)



#ordered

dict1 =   {
        "name":"Naveen",
        "rno":123456,
        "marks":455.6,
        "passRfail":True #true stands for pass      
     }

print(dict1)



#length of the dictionary

thisdict = {
  "brand": "Ford", 
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
        
  "name":"Naveen",
        
  "rno":123456,
        
  "marks":455.6,
        
  "passRfail":True #true stands for pass  
}

print(len(thisdict))
print(len(thisdict["colors"]))



#
"""
str5 = "hello"
print(len(str5))

a = 100
print(len(a))

a = 100.12
print(len(a))
"""


dict5 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


x = dict5["model"]
print(x)


#how to add extra key value pair to dictionary

dict5 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(dict5)

print("first time \n")

dict5["engine_model"] ="xyz"

print(dict5)

print("second time \n")
dict5["color"] ="Blue"

print(dict5)


#checking the items in the dictionary
print(dict5.items())



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in car:
  print("Yes,  model available")
  
if "color" in car:
  print("Yes,  model available")
else:
    print("not available")

    
#update method
dict6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict6.update({"year": 2020})
print(dict6)
  
  
#membership
# list1 = [1,2,3,4,5,6]

# print(2 in list1)

#pop mehod
dict6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


print(dict6)
dict6.pop("model")
print(dict6)


#popitem
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# del thisdict["model"]
# print(thisdict)


print("before",thisdict)
del(thisdict)

print("after",thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict.popitem()
print(thisdict)

#methods of the dictionary
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
'values'

#clear method
dict6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(dict6)

dict6.clear()
print(dict6)


#copy method

dict6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(dict6)
dict7 = dict6
dict8 = dict7

dict8["color"]="voilet"
print(dict6)
print(dict7)
print(dict8)

print()

del(dict6)
#del(dict7)
#del(dict8)

#print(id(dict6))
print("7",id(dict7))
print("8",id(dict8))
print(dict7)
print(dict8)




#
dict9 = dict6.copy()
print("6",dict6)
print("9",dict9)
dict6["seatbelt"]="yes"

print(id(dict6))
print(id(dict9))
print("after")
print("6",dict6)
print("9",dict9)


#items


dict6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


print(dict6.items())




#keys
for key in dict6:
  print(key)
  
#values
for key in dict6:
  print(dict6[key])
  
  
  
for x in dict6.keys():
  print(x)
  
  
for x, y in dict6.items():
  print(x, y)



#nesting
myfamily = {
                  "child1" : {
                    "name" : "sunil",
                    "year" : 2004
                  },
                  "child2" : {
                    "name" : "linga",
                    "year" : 2007
                  },
                  "child3" : {
                    "name" : "rajini",
                    "year" : 2011
                  }
          }


print(myfamily)
print()
print(myfamily["child1"])
print(myfamily["child2"])
print(myfamily["child3"])



print(myfamily["child1"]["name"])
print(myfamily["child2"]["name"])
print(myfamily["child1"]["year"])


myfamily = {
                  "child1" : {
                    "name" : ["jasmine","lilli","bujji"],
                    "year" : 2004
                  },
                  "child2" : {
                    "name" : "linga",
                    "year" : 2007
                  },
                  "child3" : {
                    "name" : "rajini",
                    "year" : 2011
                  }
          }


print(myfamily["child1"]["name"])
print(myfamily["child1"]["name"][0])
print(myfamily["child1"]["name"][1])
print(myfamily["child1"]["name"][2])




myfamily = {
                    "child1" : {
                                "name" : {
                                            "mylvernames":["jasmine","lilli","bujji"],
                                            "giftsgiven":["rose","vodka","pen"]
                                        
                                        },
                                "year" : 2004
                  },
                  "child2" : {
                    "name" : "linga",
                    "year" : 2007
                  },
                  "child3" : {
                    "name" : "rajini",
                    "year" : 2011
                  }
          }

print(myfamily["child1"]["name"]["giftsgiven"][1])
print(myfamily["child1"]["name"]["mylvernames"])
print(myfamily["child1"]["name"]["mylvernames"][0])
print(myfamily["child1"]["name"]["mylvernames"][1])
print(myfamily["child1"]["name"]["mylvernames"][2])
print(myfamily["child1"]["name"]["mylvernames"][-1])




# list1 = [1,2,3,[4,5,6,[7,8,9]]]
# print(list1[1])
# print(list1[3])



# print(list1[3][3])
# print(list1[3][3][1])
# print(list1[1])


#interview questions


dict6 = {
  "brand": "Ford",
  "brand": "suzuki",
  "model": "Mustang",
  "year": 1964
}

print(dict6["brand"])


#question2:
    
dict6 = {
  "brand": "Ford",
  "color": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(dict6["color"])


#question3

dict6 = {
  "key1": "Ford",
  "key2": "Ford",
  "model": "Mustang",
  "key3": 1964,
  "key2": 123,
}
print(dict6["key2"])

#question4
dict1 = {
        (3,4,8):4,
        (5,6,9):3
        }
print('output:',dict1[5,6,9])























































    
















#interview question

how you will create empty dictionary

dict2 = {}
print(dict2)
print(type(dict2))

dict3 = {1,2,3}
print(dict3)
print(type(dict3))


#tuples to list and to dictionary
dict4 = dict([(1,'Geeks'),(2,'For'), (3,'Geeks')])

print(dict4)














 


     