# Python Program To Show Single Tasking Using A Thread That Prepares Tea
# Single Tasking Using A Single Thread

'''
Function Name    :  Show Single Tasking Using A Thread That Prepares Tea
Function Date    :  3 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from threading import*
from time import*

# Create Our Own Class

class MyThread:
    
    # A Method That Perform 3 Tasks One By One
    
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()
        
    def task1(self):
        print('Boil Milk And Tea Powder For 5 Minutes...', end='')
        sleep(5)
        print('Done')
        
    def task2(self):
        print('Add Sugar And Boil For 3 Minutes...', end='')
        sleep(3)
        print('Done')
        
    def task3(self):
        print('Filter It And Serve...', end='')
        print('Done')
        
# Create An Instance To Our Class

obj = MyThread()

# Create A Thread And Run PrepareTea Method Of obj

t = Thread(target=obj.prepareTea)
t.start()
