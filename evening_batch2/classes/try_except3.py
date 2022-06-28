# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:38:17 2022

@author: durga
"""
try:
        
    import os
    import sys
    import anil
    import meghana
    import ramcharan
    import bahubali
except:
    print("this is my testing of try except finally")

import abc

class food(abc.ABC):
    @abc.abstractmethod
    def taste(self):
        print("this is testing")

class fast_food(food):
    def taste(self):
        print("tasty in fastfood")
    
a_obj = fast_food()
print(isinstance(a_obj, food))



#example2


import abc

class myclass(abc.ABC):
    @abc.abstractmethod
    def calling(self):
        print("this is calling method")
    
class room(myclass):
    def calling(self):
        print("this is testing")
        
        
        
a_obj = room()


# =============================================================================
# 
# =============================================================================
try:
        
    import os
    import sys
    import anil
    import meghana
    import ramcharan
    import bahubali
except:
    print("this is my testing of try except finally")
    sys.exit()


# =============================================================================
# 
# =============================================================================
try:
        
    import os
    import sys
    #import anil
    #import meghana
    #import ramcharan
    #import bahubali
    
    print("end of the try block")
    
    
except:
    print("this is my testing of try except finally")
    sys.exit()


# =============================================================================
# 
# =============================================================================

try:
        
    import os
    import sys
   
    a =20
    b =10
    print(a+b)
    print(a/0)
    print("end of the try block")
    
except:
    print("this is my testing of try except finally")
    sys.exit()

try:
    import abc
    
    class myclass(abc.ABC):
        @abc.abstractmethod
        def calling(self):
            print("this is calling method")
        
    class room(myclass):
        def calling(self):
            print("this is testing")
            
                
    a_obj = room()
    print("this is end of the program")
except:
    print("this is my testing of try except finally")
    sys.exit()
    

