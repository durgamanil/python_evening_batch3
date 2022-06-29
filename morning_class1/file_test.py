# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 06:55:56 2022

@author: durga
"""

# import os


# file1 = open("test123.txt")

# print(file1)

# file1 = open("img.jpg")

# print(file1)
# print(file1.read())

# file1 = open("employee_class.py")

# print(file1)
# print(file1.read())

# =============================================================================
# 
# =============================================================================

# file2 = open("D:/python/Evening_batch/entry_test.py")
# print(file2)
# print(file2.read())

# =============================================================================
# file modes
# =============================================================================
# r = read default
# a = append mode
# w = write mode and opens also
# x = create  new


# file1 = open("test.txt",'r')
# print(file1)
# print(file1.read())


# file1 = open("test.txt",'a')
# print(file1)

file1 = open("test.txt",'w')
print(file1)

for i in range(100,200):
    file1 = open(f"test6{i}.txt",'x')
    print(file1)

#t= text default, text mode
#b= binary mode..(images)


# file1 = open("test.txt",'r')
# print(file1.read())



# file2 = open("D:/python/morning_class/test7.txt",'r')
# print(file2.read())

# file2 = open("D:/python/morning_class/test.txt",'r')
# print(file2.read(7))

# file2 = open("D:/python/morning_class/test.txt",'r')
# print(file2.read(10))

# =============================================================================
# readline()
# =============================================================================
# file2 = open("D:/python/morning_class/test.txt",'r')
# print(file2.readline())
# print(file2.readline())
# print(file2.readline())
# print(file2.readline())
# print(file2.readline())




# file2 = open("D:/python/morning_class/test.txt",'r')
# print(file2.readline(10))
# print(file2.readline(7))

# =============================================================================
# close the files
#variable.close()
# =============================================================================
file2 = open("D:/python/morning_class/test.txt",'r')
print(file2.readline(10))
# file2.close()
# print(file2.readline(10))


# =============================================================================
# write the extra lines
#variable.write()
# =============================================================================
file2 = open("D:/python/morning_class/test.txt",'a')
file2.write("extraline append to  nextline")

file2 = open("D:/python/morning_class/test.txt",'r')
print(file2.read())
file2.close()

#file2 = open("D:/python/morning_class/test.txt",'r')
print(file2.read())


file2 = open("D:/python/morning_class/test9.txt",'x')
file2.write("extraline append to  nextline")

# file2 = open("D:/python/morning_class/test9.txt",'r')
# print(file2.read())
# file2.close()


# a= dir(os)
# print(a)

#CRUD----create,read,update,delete
# os.remove("test7.txt")
















