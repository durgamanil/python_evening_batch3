# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:23:44 2022

@author: durga
"""
import math

n = 7608456768
a =[(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]

print(len(a))
print(a)
