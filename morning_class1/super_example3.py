# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 06:50:21 2022

@author: durga
"""

class A:
  def __init__(self, Animal):
    print(Animal, 'is an animal.')

class B(A):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class C(B):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)
    
class D(B):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    #B.__init__(self)
    super().__init__(NonMarineMammal)

class Dog1(D,B,C):
  def __init__(self):
    print('Dog has 4 legs.')
    #D.__init__(self)
    #C.__init__(self)
    super().__init__('Dog')
    
    
# class Dog1(D,C):
#   def __init__(self):
#     print('Dog has 4 legs.')
#     #D.__init__(self)
#     #C.__init__(self)
#     super().__init__('Dog')
    
d = Dog1()
print(Dog1.mro())
print('')
#bat = D('Bat')





# class A:
#   def __init__(self, Animal):
#     print(Animal, 'is an animal.')

# class B(A):
#   def __init__(self, mammalName):
#     print(mammalName, 'is a warm-blooded animal.')
#     super().__init__(mammalName)
    
# class C(B):
#   def __init__(self, NonWingedMammal):
#     print(NonWingedMammal, "can't fly.")
#     super().__init__(NonWingedMammal)

# class D(B):
#   def __init__(self, NonMarineMammal):
#     print(NonMarineMammal, "can't swim.")
#     #B.__init__(self)
#     super().__init__(NonMarineMammal)

# class Dog1(D):
#   def __init__(self):
#     print('Dog has 4 legs.')
#     #D.__init__(self)
#     #C.__init__(self)
#     super().__init__('Dog')
    
# #d = Dog1()
# print(Dog1.mro())
# print('')
# #bat = D('Bat')