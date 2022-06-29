# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 06:21:59 2022

@author: durga
"""

# Python program to demonstrate
# super function

class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    
d1 = Dog()





class Animals:	
	# Initializing constructor
	def __init__(self):
		self.legs = 4
		self.domestic = True
		self.tail = True
		self.mammals = True
	
	def isMammal(self):
		if self.mammals:
			print("It is a mammal.")
	
	def isDomestic(self):
		if self.domestic:
			print("It is a domestic animal.")
	
class Dogs(Animals):
	def __init__(self):
		super().__init__()

	def isMammal(self):
		super().isMammal()

class Horses(Animals):
	def __init__(self):
		super().__init__()

	def hasTailandLegs(self):
		if self.tail and self.legs == 4:
			print("Has legs and tail")

# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()






