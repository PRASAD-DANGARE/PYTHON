'''
Description      :  Multiprocessing 
Function Date    :  14 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

import os
import multiprocessing

def Process1(no):
    print("Process 1 is created")
    print("PID of process 1 is : ", os.getpid())
    print("PID of parent process of process1 is ", os.getppid())
    for i in range(no):
        print("Process-1 ", i)

def Process2(no):
    print("Process 2 is created")
    print("PID of process 2 is : ", os.getpid())
    print("PID of parent process of process2 is ", os.getppid())
    for i in range(no):
        print("Process-2 ", i)

def main():
    print("Inside Main Process")

    print("PID of current is ", os.getpid())

    print("PID of parent process of main is ", os.getppid())

    value = 10
    p1 = multiprocessing.Process(target = Process1, args = (value,))
    p2 = multiprocessing.Process(target = Process2, args = (value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")

if __name__ == "__main__":
    main()