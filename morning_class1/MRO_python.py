# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 07:04:31 2022

@author: durga
"""

# Demonstration of MRO
#method order resolution

class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Z, Y):
    pass


class M(B,A,Z):
    pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
#  <class '__main__.A'>, <class '__main__.X'>,
#  <class '__main__.Y'>, <class '__main__.Z'>,
#  <class 'object'>]

#print(M.mro())
print(A.mro())



#o/p
# [<class '__main__.M'>,
#  <class '__main__.B'>,
#  <class '__main__.A'>,
#  <class '__main__.X'>, 
#  <class '__main__.Y'>, 
#  <class '__main__.Z'>,
#  <class 'object'>]