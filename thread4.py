# Python Program To Create A Thread By Making Our Class As Sub Class To Thread Class

'''
Function Name    :  Create A Thread By Making Our Class As Sub Class To Thread Class
Function Date    :  3 Oct 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from  threading import Thread # Create Our Own Thread

# Create A Class As Sub Class To Thread Class

class MyThread(Thread):
    
    # Override The run() Method Of Thread Class
    
    def run(self):
        for i in range(1, 6):
            print(i)
            
# Create An Instance Of MyThread Class

t1 = MyThread()

# Start Running The Thread t1

t1.start()

# Wait Till The Thread Completes Execution

t1.join()
