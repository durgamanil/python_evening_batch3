# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:03:24 2022

@author: durga
"""

# =============================================================================
# files
# =============================================================================


file_var = open("test.txt")
print(file_var)

modes
"r"----> read mode...default 
"a"---->append mode
"w"----> write mode
"x"--->create the file

syntax:
    open("file_path+filename.extention",mode="r")
    
    
file_var = open("test.txt","r")

print(file_var.read())


#fullpath
D:\python\evening_batch2\files

file_var = open("D:\\python\\evening_batch2\\files\\test.txt","r")

print(file_var.read())


#D:\python\evening_batch2

file_var = open("D:\python\evening_batch2\\test3.py","r")

print(file_var.read())

#images will not opened directly
file_var = open("D:\\python\\evening_batch2\\files\\laddu.jpg","r")

print(file_var.read())


#

file_var = open("D:\\python\\evening_batch2\\files\\test.txt","r")

print(file_var.read(5))


file_var = open("D:\\python\\evening_batch2\\files\\test.txt","r")

print(file_var.read(7))


file_var = open("D:\\python\\evening_batch2\\files\\test.txt","r")

print(file_var.read(20))


file_var = open("D:\\python\\evening_batch2\\files\\test.txt","r")

print(file_var.read(100))



file_var = open("D:\\python\\evening_batch2\\files\\test.txt","r")

print(file_var.read(1000))


file_var = open("D:\\python\\evening_batch2\\files\\index.html","r")

print(file_var.read())


a=10+30

print(a)


#append--->add end of the line

file1 = open("D:\\python\\evening_batch2\\files\\test.txt","a")

file1.write("this,word,this,word")



file_var = open("D:\\python\\evening_batch2\\files\\test.txt","r")

print(file_var.read())


#readline()
#methods of file
['_CHUNK_SIZE',
 '__class__',
 '__del__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__enter__',
 '__eq__',
 '__exit__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__next__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '_checkClosed',
 '_checkReadable',
 '_checkSeekable',
 '_checkWritable',
 '_finalizing',
 'buffer',
 'close',
 'closed',
 'detach',
 'encoding',
 'errors',
 'fileno',
 'flush',
 'isatty',
 'line_buffering',
 'mode',
 'name',
 'newlines',
 'read',
 'readable',
 'readline',
 'readlines',
 'reconfigure',
 'seek',
 'seekable',
 'tell',
 'truncate',
 'writable',
 'write',
 'write_through',
 'writelines']


file_var = open("D:\\python\\evening_batch2\\files\\test.txt","r")

print(file_var.readline())
print(file_var.readline())
print(file_var.readline())
print(file_var.readline())



#readlines()

file_var = open("D:\\python\\evening_batch2\\files\\test.txt","r")

print(file_var.readlines(1))



file_var = open("D:\\python\\evening_batch2\\files\\test2.txt","r")

print(file_var.readlines(3))
#print(file_var.readlines())



#ctrl+mouse left click


#write

file_var = open("D:\\python\\evening_batch2\\files\\test2.txt","w")

file_var.write("this is testing by evening batch11")

file_var = open("D:\\python\\evening_batch2\\files\\test2.txt","r")

file_var.read()


#x

file2 = open("mytest1.txt","x")
file2 = open("mytest2.pdf","x")
file2 = open("mytest3.doc","x")




file2 = open("file11.txt","x")
file3 = open("file11.txt","x")






for i in range(0,100):
    file1 = open(f"tests{i}.txt","x")
    
    file1 = open(f"tests{i}.txt","w")
    file1.write("Hello meghana")
    file1.close()
    
    
import os   
#os.remove("file10.txt")
#os.remove("tests3.txt")
os.removedirs("anil")
    
    


a =1
b =2
c =3
d= 4
    
#print("this is testing--{},{},{},{}".format(a,b,c,d))


print(f'this is testing {a},{b},{c},{d}')
print(f"this is testing {a},{b},{c},{d}")
print(F'this is testing {a},{b},{c},{d}')
print(F"this is testing {a},{b},{c},{d}")



for i in range(0,100):
    open(f"test{i}.txt","x")
    

















