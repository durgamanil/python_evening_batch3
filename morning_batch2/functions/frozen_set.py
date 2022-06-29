#frozenset() is the inbuilt function that will take 1 argument
#iterable argument

#tuple
tupel1 = (1,2,3,4,5)
var1 = frozenset(tupel1)
print(var1)

#empty frozenset
print("this is empty forzenset===>",frozenset())

#add elements to the forzenset

#var1.add(6)
#print(var1)

#dictionary
dict1 = {"name":"raju",
            "age":30,
            "gender":"male",
            "study":"mtech"}

frs1 =frozenset(dict1)
print(frs1)

dir(frozenset)
#copy 
#union
#intersection
#difference
#symmetric_difference