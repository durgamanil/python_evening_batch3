# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 08:06:25 2022

@author: durga
"""

# Nesting
# ===========================

# syntax:
    
# if condition:
#     if condition:
#         if condition:
#             """statements"""
#         else:
#             if condition:
#                 """statements"""
                

marks = int(input("please enter your marks"))
if marks>80 and marks <100:
    if marks>95 and marks <100:
        print("your marks",marks)
    if marks >90 and marks< 95:
        print("your marks",marks)
        
        
        
        

            
            
            