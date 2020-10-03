# Python Program To Create A Thread That Accesses The Instance Variables Of A Class

'''
Function Name    :  Create A Thread That Accesses The Instance Variables Of A Class
Function Date    :  3 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from threading import*

# Create A Class As Sub Class To Thread Class

class MyThread(Thread):
    
    # Constructor That Calls Thread Class Constructor
    
    def __init__(self, str):
        Thread.__init__(self)
        self.str = str
        
    # Override The run() Method Of Thread Class
    
    def run(self):
        print(self.str)
        
    # Create An Instance Of MyThread Class And Pass The String
    
    t1 = MyThread('Hello')
    
    # Start Running The Thread t1
    
    t1.start()
    
    # Wait Till The Thread Completes Execution
    
    t1.join()