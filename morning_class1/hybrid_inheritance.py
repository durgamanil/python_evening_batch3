# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 07:38:35 2022

@author: durga
"""

class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X):
    pass

class B(A):
    pass


class M(B,A,Z):
    pass

class N(X):
    pass

#print(N.mro())
print(M.mro())

