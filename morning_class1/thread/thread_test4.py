# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:37:26 2022

@author: durga
"""


import threading
import os
import time


start_time = time.time()

def task1(num):
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    print("Cube: {}".format(num * num * num * num))
    for i in range(100):
        print("inside task1")
    
def task2(num):
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
    print("Square: {}".format(num * num))
    for i in range(100):
        print("inside task2")
    
    
def task3(num):
    print("Task 3 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 3: {}".format(os.getpid()))
    print("Square: {}".format(num + num))
    for i in range(100):
        print("inside task3")
    
if __name__ == "__main__":
    
    #print("start_time",start_time)
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

	# print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

	# creating threads
    t1 = threading.Thread(target=task1, name='t1',args=(10,))
    t2 = threading.Thread(target=task2, name='t2',args=(10,))
    t3 = threading.Thread(target=task3, name='t3',args=(10,))
	# starting threads
    t1.start()
    t2.start()
    t3.start()
	# wait until all threads finish
    t1.join()
    t2.join()
    t3.join()
    total_time = time.time()-start_time
    print(total_time)
    print("this is end of the line")