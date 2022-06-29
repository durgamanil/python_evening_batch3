def name():
    print("this is inside name function")
    
def fun1(name):
    print("this is testing")
    name()
    

if __name__ == '__main__':
    print("this is main function")
    fun1(name)