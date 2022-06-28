# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:47:44 2022

@author: durga
"""

# =============================================================================
# super keyword
# =============================================================================


#syntax:
    class a:
        """statement"""
    class b(a):
        super().__init__()
        
        
        
class a:
    def __init__(self):
        print("this is the a class")
        
class b(a):
    def __init__(self):
        super().__init__()
        

m_obj = b()


#single inheritance

class a:
    def __init__(self):
        print("this is the a class")
    def test(self):
        print("this is testmethod")
        
class b(a):
    def __init__(self):
        a.__init__(self)
        

m_obj = b()
m_obj.test()

# =============================================================================
# 
# =============================================================================

class parent:
    def __init__(self):
        self.id = 4
        self.name= "charan"
        print("this is end of the default constructor")
        
    def house(self):
        if self.name =="charan":
            print("this is charan house")
            
            
class child(parent):
    def __init__(self):
        super().__init__()
        
        

ch_obj = child()
ch_obj.house()
    
# =============================================================================
# 
# =============================================================================
class parent:
    def __init__(self):
        self.id = 4
        self.name= "charan"
        print("this is end of the default constructor")
        
    def house(self):
        if self.name =="charan":
            print("this is charan house")
            
            
class child1(parent):
    def __init__(self):
        super().__init__()
        
class child2(child1):
    def __init__(self):
        super().__init__()
        
        

ch_obj = child1()
ch_obj.house()
    