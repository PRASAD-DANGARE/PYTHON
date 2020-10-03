# Python Program That Perform Two Tasks Using Two Threads Simultaneously

'''
Function Name    :  Perform Two Tasks Using Two Threads Simultaneously
Function Date    :  3 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from threading import*
from time import*

class Theatre:
    
    # Constructor That Accepts A String
    
    def __init__(self, str):
        self.str = str
        
    # A Method That Repeats For 5 Times
    
    def movieshow(self):
        for i in range(1, 6):
            print(self.str, " : ",i)
            sleep(0.1)
            
# Create Two Instance To Thread Class

obj1 = Theatre('Cut Ticket')
obj2 = Theatre('Show Chairs')

# Create Two Threads To Run movieshow()

t1 = Thread(target=obj1.movieshow)
t2 = Thread(target=obj2.movieshow)

# Run The Thread

t1.start()
t2.start()

