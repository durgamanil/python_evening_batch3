# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 07:04:14 2022

@author: durga
"""


# class C:
#   def __init__(self, NonWingedMammal):
#     print(NonWingedMammal, "can't fly.")
#     #super().__init__(NonWingedMammal)

# class D(C):
#   def __init__(self, NonMarineMammal):
#     print(NonMarineMammal, "can't swim.")
#     #C.__init__(self)
#     super().__init__(NonMarineMammal)
    
    
# class Dog1(D):
#   def __init__(self):
#     print('Dog has 4 legs.')
#     #D.__init__(self,NonWingedMammal)
#     #C.__init__(self,NonMarineMammal)
#     super().__init__('Dog')
    
# d = Dog1()
# #print(Dog1.mro())



class C:
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    #super().__init__(NonWingedMammal)

class D(C):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    #C.__init__(self)
    super().__init__("dabarman")
    
    
class Dog1(D):
  def __init__(self):
    print('Dog has 4 legs.')
    #D.__init__(self,NonWingedMammal)
    #C.__init__(self,NonMarineMammal)
    super().__init__('Dog')
    
d = Dog1()
#print(Dog1.mro())