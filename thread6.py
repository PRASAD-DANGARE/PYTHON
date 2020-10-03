# Python Program To Create A Thread That Act On The Objects Of A Class 
# That Is Not Derived From The Thread Class

'''
Function Name    :  Creating Thread Without Sub Class To Thread Class
Function Date    :  3 Oct 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''


from threading import*

class MyThread:
    
    # A Constructor 
    
    def __init__(self, str):
        self.str = str
        
    # A Method
    
    def display(self, x, y):
        print(self.str)
        print('The args Are : ', x, y)
        
# Create An Instance To Our Class And Store 'Hello' String

obj = MyThread('Hello')

# Create A Thread To Run Display Method Of obj

t1 = Thread(target=obj.display, args=(1, 2))

# Run The Thread 

t1.start()