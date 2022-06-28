# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:54:25 2022

@author: durga
"""

import gc

print(dir(gc))

['DEBUG_COLLECTABLE',
 'DEBUG_LEAK', 
 'DEBUG_SAVEALL', 
 'DEBUG_STATS', 
 'DEBUG_UNCOLLECTABLE',
 '__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__', 
 'callbacks', 
 'collect', 
 'disable', 
 'enable',
 'freeze',
 'garbage',
 'get_count', 
 'get_debug',
 'get_freeze_count',
 'get_objects',
 'get_referents',
 'get_referrers',
 'get_stats', 
 'get_threshold',
 'is_finalized',
 'is_tracked',
 'isenabled', 
 'set_debug',
 'set_threshold',
 'unfreeze']


print("this is get count",gc.get_count())
print("this is get threshold",gc.get_threshold())




import gc

collected = gc.collect()
print("this is collection",collected)




# =============================================================================
# 
# =============================================================================

import gc

i =0

def create_cycle():
    x ={}
    x[i+1]= x
    print(x)
    
collected = gc.collect()
print("this is collection",collected)


print("this colletion cycle")
for i in range(10):
    create_cycle()
    

collected = gc.collect()
print("this is collection",collected)
    





















