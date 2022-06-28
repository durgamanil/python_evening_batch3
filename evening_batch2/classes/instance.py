# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:19:20 2022

@author: durga
"""

# =============================================================================
# interfaces

#informal 
#formal--->ABCs(abstract base class)
# =============================================================================


#informal
#example:
    
class cookies:
    def __init__(self, items):
        self.__items = items
        
    def __len__(self):
        return len(self.__items)
    
    def __contain__(self,items):
        return items in self.__items
    
    
my_cook_obj = cookies(["marygold","tiger","good_day","fifty_fifty"])  

print(len(my_cook_obj))
#print("marygold" in my_cook_obj)
print("dairymilk" not in my_cook_obj)


    

    
# =============================================================================
# 
# =============================================================================

class cookies:
    def __init__(self, items):
        self.items = items
        
    def __len__(self):
        return len(self.items)
    
    def __contain__(self,items):
        return items in self.items
    
    
my_cook_obj = cookies(["marygold","tiger","good_day","fifty_fifty"])  

print(len(my_cook_obj))
    
#print(len(["marygold","tiger","good_day","fifty_fifty"]) ) 

list2 =["marygold","tiger","good_day","fifty_fifty"]

print("marygold" in list2)
print("dairy milk" in list2)
        
        
# =============================================================================
# 
# =============================================================================
# name ----->general
# _name----->secure
# __name ====> more secure
# __name__ ===>more secure
