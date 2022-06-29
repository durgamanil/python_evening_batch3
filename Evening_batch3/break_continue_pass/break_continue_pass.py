# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 20:40:41 2022

@author: durga
"""

# =============================================================================
# Break continue pass
# =============================================================================

#break will stop the execution at  when it reaches the break keyword

syntax:
    
    for i  in range:
        #print(i)
        if condtion:
            break
        

example

for i  in range(0,100):
    print(i)
    if i == 50:
        break
    
for i  in range(0,100):
    print(i)
    if i == 10:
        break    

i = 1
while i <20:
    i = i +1
    print(i) 
    if i == 10:
        print("testing")
        break
    
    
#continue
it will continue the loops
#continue also keyword

for i  in range(0,100):
    #
    if i >= 50:
        print(i)
        continue
    

for i  in range(0,100):
    if i < 10:
        print(i)
        break
    if i >= 50:
        print(i)
        continue


# =============================================================================
# pass ----
# =============================================================================
#if you dnot have certain information about the block
#you can write pass keyword  


for i  in range(0,100):
    pass
 
if 10<20:
    pass


def fun1():
    pass


fun1()