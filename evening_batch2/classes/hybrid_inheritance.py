# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:53:46 2022

@author: durga
"""

# =============================================================================
# hybrid inheritance
# =============================================================================
syntax:
    
    class a:
        """statements"""
    class b(a):
        """statments"""
    class c(a):
        """statements"""
    class d(c,a):
        """statements"""
        
        
#example:
    
class institute:
    def fun1(self):
        print("this is the institute class")
        
class student1(institute):
    def  fun2(self):
        print("this is the student1 class")
        
class student2(institute):
    def fun3(self):
        print("this is student2 class")
        
class student3(student1,institute):
    def fun4(self):
        print("this is the student3 class")
        
        
s_obj = student3()
s_obj.fun2()
#s_obj.fun1()
s_obj.fun4()


today assignment:
    remove _default constructors and check all the methods of every inheritance
    
    
hybrid_inheritance:
    parent_child_class....need to create two methods for each method
    default construtor
    
    
    
    
    
    

            
        
        
        
        
        