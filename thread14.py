# Python Program That Uses A Queue In Thread Communication

'''
Function Name    :  Uses A Queue In Thread Communication
Function Date    :  5 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import queue
from threading import*
from time import*
from queue import*

# Create Producer Class

class Producer:
    def __init__(self):
        self.q = Queue()
        
    def produce(self):
        
        # Create 1 To 10 Items And Add To The Queue
        
        for i in range(1, 11):
          print('Producing Items : ', i)
          self.q.put(i)
          sleep(1)
          
# Create Consumer Class

class Consumer:
    def __init__(self, prod):
        self.prod = prod
        
    def consume(self):
        
        # Receive 1 To 10 Items From The Queue
        
        for i in range(1, 11):
            print('Receving Items : ', self.prod.q.get(i)) 
            
# Create Producer Object

p = Producer()

# Create Consumer Object And Pass Producer Object

c = Consumer(p)

# Create Producer And Consumer Threads

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

# Run The Threads

t1.start()
t2.start()


        

        