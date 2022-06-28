# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:56:28 2022

@author: durga
"""
try:
        
    import os
    import sys
    import anil
    import vandana
    import charan
    import sridevi
    
except Exception as err :
    print("importing library error",err)



#try except finally


try :
    print("connection code")
except:
    print("network issue")
    sys.exit()
#try except else finally




import pymysql

# =============================================================================
# how to check the methods of the pymysql
# =============================================================================


try:
    
    # To connect MySQL database
    conn = pymysql.connect(host='localhost',user='root',password = "",db='atm_project')
    cursor1 = conn.cursor()
    print(cursor1)
    
except Exception as err:
    print(err)
    
finally:
    print("this is the finally block")
    conn.close()
    
    


# =============================================================================
# 
# =============================================================================
# =============================================================================
# how to check the methods of the pymysql
# =============================================================================


try:
    
    # To connect MySQL database
    conn = pymysql.connect(host='localhost',user='root',password = "",db='atm_project')
    cursor1 = conn.cursor()
    print(cursor1)
    
except Exception as err:
    print(err)
    
else:
    print("this is else block")
    
finally:
    print("this is the finally block")
    conn.close()