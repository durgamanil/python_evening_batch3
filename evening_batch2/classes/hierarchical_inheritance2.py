# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:08:45 2022

@author: durga
"""

# =============================================================================
# hierarchical inheritance
# =============================================================================

syntax:
    class a:
        """statements"""
        
    class b(a):
        """statments"""
    class c(a):
        """statements"""
        
        
class parent:
    def __init__(self):
        print("This is parent class")
        
class child1(parent):
    def __init__(self):
        parent.__init__(self)
        print("this is the child1 class")
        
class child2(parent):
    
        def __init__(self):
            parent.__init__(self)
            print("this is the child2 class")
            
            
a_obj = child2()
b_obj = child1()



# =============================================================================
# with out default constructor
# =============================================================================
class parent:
    def fun1(self):
        print("this is parent class")
        
class child1(parent):
    def __init__(self):
        parent.__init__(self)
        print("this is the child1 class")
        
class child2(parent):
    
        def __init__(self):
            parent.__init__(self)
            print("this is the child2 class")
            
            
a_obj = child2()
b_obj = child1()



# =============================================================================
# with out default constructor
# =============================================================================
class parent:
    def fun1(self):
        print("this is parent class fun1")
        
    def fun2(self):
        print("this is parent class fun2")
        
        
a_obj = parent()
a_obj.fun1()
a_obj.fun2()


# =============================================================================
# with out default constructor calling methods
# =============================================================================
class parent:
    def fun1(self):
        print("this is parent class")
        
class child1(parent):
    def __init__(self):
        parent.__init__(self)
        print("this is the child1 class")
        
    def fun2(self):
        print("this is fun2 method from child1 ")
        
class child2(parent):
    
        def __init__(self):
            parent.__init__(self)
            print("this is the child2 class")
            
        def fun3(self):
            print("this is fun2 method from child2 ")
            
            
a_obj = child2()
b_obj = child1()
a_obj.fun1()
b_obj.fun1()
b_obj.fun2()
a_obj.fun3()

# =============================================================================
# 
# =============================================================================

class parent:
    def fun1(self):
        print("this is parent class")
        
    def fun4(self):
        print("this is parent class4")
        
    def fun5(self):
        print("this is parent class5")
        
class child1(parent):
    def __init__(self):
        parent.__init__(self)
        print("this is the child1 class")
        
    def fun2(self):
        print("this is fun2 method from child1 ")
        
         
    
class child2(parent):
        def __init__(self):
            parent.__init__(self)
            print("this is the child2 class")
            
        def fun3(self):
            print("this is fun2 method from child2 ")
            
            
a_obj = child1()
a_obj.fun2()
a_obj.fun4()
a_obj.fun5()







    





