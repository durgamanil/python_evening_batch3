# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 07:05:03 2022

@author: durga
"""

import my_calculator_basic_functions_sub_div_mul_add as calc
import utility_math
import utility_email

# import pandas as pd
# import numpy as np
# import tkinter as tk
# import tensorflow as tf



#from my_calculator_basic_functions_sub_div_mul_add import add_fn


#print(id(my_calculator_basic_functions_sub_div_mul_add))
print(id(calc))

calc.add_fn(10,40)
calc.div_fn(40, 4)
calc.mul_fn(60, 50)
calc.sub_fn(80, 40)

utility_email.add_fun2(10, 40)

# my_calculator_basic_functions_sub_div_mul_add.add_fn(10,40)

# my_calculator_basic_functions_sub_div_mul_add.add_fn(10,60)

# my_calculator_basic_functions_sub_div_mul_add.sub_fn(30, 50)

# my_calculator_basic_functions_sub_div_mul_add.mul_fn(5000, 15)