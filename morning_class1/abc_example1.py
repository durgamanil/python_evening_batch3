# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 07:47:16 2022

@author: durga
"""

# =============================================================================
# example 4
# =============================================================================
# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod

class A(ABC):
	def fun1(self):
		print("Abstract Base Class")

class K(A):
	def fun2(self):
		super().fun1()
		print("subclass ")

# Driver code
r = K()
r.fun2()