# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 18:11:50 2022

@author: durga
"""


f = open('checkin1.txt','x')
print("checkin1.txt is created")

#for read the file, we need to open in the read mode ie: 'r'
f = open('checkin.txt','r')
print(f.read())
#must have exactly one of create/read/write/append mode
