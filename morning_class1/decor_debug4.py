# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 07:26:48 2022

@author: durga
"""
def name():
    print("this is inside name function")
    
def fun1(name):
    print("this is testing")
    name()
    

if __name__ == '__main__':
    print("this is main function")
    fun1(name)