# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:16:44 2022

@author: durga
"""

# =============================================================================
# Nesting
# =============================================================================


marks = 45

if marks > 60:
    if marks >70:
        print("first class")
    else:
        print("marks above 60")
    
elif marks < 60 and marks>50:
    if marks >70:
        print("first class")
    else:
        print("marks above 60")
    print("second class")
    
else:
    
    if marks >70:
        print("first class")
    else:
        print("marks above 60")
    print("just pass")
