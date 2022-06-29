#two arguments

def addition(a,b):#Zero arguments based function
    """
    This function will greet the person
    """
    print("Good morning ")  
    c = a + b #local  variable
    print(c)
    
if __name__ == "__main__":
    addition(10,20) 
    #print(c)

#global variable
c = 0 

def addition(a,b):#Zero arguments based function
    """
    This function will greet the person
    """
    print("Good morning ")  
    c = a + b #local  variable
    print(c)
    
if __name__ == "__main__":
    print(c)
    addition(10,20) 
    print(c)
    
# =============================================================================
#    
# =============================================================================
c = 0 

def addition(a,b):#Zero arguments based function
    """
    This function will greet the person
    """
    print("Good morning ")  
    c = a + b #local  variable
    print(c)
    print(id(c))
    
if __name__ == "__main__":
    print(c)
    print(id(c))
    addition(10,20) 
    print(c)
    print(id(c))
    
# =============================================================================
# return
# =============================================================================
c = 0
def addition(a,b):#Zero arguments based function
    """
    This function will greet the person
    """
    print("Good morning ")  
    c = a + b #local  variable
    print(c)
    print(id(c))
    return c 
    
if __name__ == "__main__":
    print(c)
    print(id(c))
    return_var = addition(10,20) 
    print(c)
    print(id(c))
    print(return_var)
    
# =============================================================================
# global 
# =============================================================================
#global is keyword
#it will declare any variable as global

def addition(a,b):#Zero arguments based function
    global c
    c = a + b #local  variable
    print(c)
    print(id(c))
    return c 
    
if __name__ == "__main__":

    return_var = addition(10,20) 
    print(c)
    print(id(c))
    print(return_var)  