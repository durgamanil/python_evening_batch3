# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 20:38:34 2022

@author: durga
"""

for i in range(0,101,2):
    print("this is testing",i)
    
for i in range(101):
    print("this is testing",i)
    
for i in range(100,101):
    print("this is testing",i)
    
for i in range(-1,5,1):
    print(i)
    
for i in range(-1,-5,-1):
    print(i)
    

#nesting
for i in range(0,5,1):
    #print(i,end='')
    for j in range(0,5,1):
        print("i=", i,"j=",j)
        
        
for i in range(0,5,1):
    for j in range(0,5,1):
        print("*")
        
        
for i in range(0,5,1):
    for j in range(0,5,1):
        print("*",end='')


for i in range(0,5,1):
    for j in range(0,5,1):
        print("*",end='')
    print()
    
for i in range(0,5,1):
    for j in range(0,5,1):
        
        #print("*",end='')
        print("i=", i,"j=",j,end='')
    print()   
    
for i in range(0,5,1):
    for j in range(0,5,1):
        # if (i == j):
        #     pass
        if (j<=i):
            print("*",end='') 
    print()   
      
   

assignments:        
*
**
***
****
*****

assignments2:
*****
****
***
**
*

assignments3:
    *
   **
   ***
   ****
   
a
aa
aaa
aaaa
aaaaa


1
12
123
1234
12345

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    