# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:46:33 2022

@author: durga
"""


# =============================================================================
# break
# =============================================================================

a =1

while a <= 2000:
    print(a)
    a = a+1
    if a ==1000:
        break
    



for i in range(1,10000,1):
    print(i)
    if i == 5000:
        break
    
    
# =============================================================================
# continue
# =============================================================================
for i in range(1,100,1):
    #print(i)
    if i >= 50:
        print(i)
        continue


i =1
while i <100:
    i = i +1 #i +=1
    if i >=50:
        print(i)
        continue
    
    
i =1
while i <10:
    print("after while")
    i = i +1 
    
    if i ==5:
        
        print("inside if ",i)
        continue
    
    
# =============================================================================
# pass
# =============================================================================
for i in range(1,10000,1):
    #print(i)
    pass

while i <= 10:
    pass


if i <=10:
    pass


def evening_class():
    pass