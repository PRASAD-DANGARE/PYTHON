# Python Program Where Thread Communication Is Done Through Notify() And Wait() Methods Of Condition Object

'''
Function Name    :  Thread Communication Is Done Through Notify() And Wait()
Function Date    :  5 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String,Integer
'''

from threading import*
from time import*

# Create Producer Class

class Producer:
  def __init__(self):
    self.lst = []
    self.cv = Condition()
    
  def produce(self):
    
    # Lock The Condition Object
    
    self.cv.acquire()
    
    # Create 1 To 10 Items And Add To The List
    
    for i in range(1, 11):
        self.lst.append(i)
        sleep(1)
        print('Item Produced...')
        
    # Inform The Consumer That Production Is Completed
    
    self.cv.notify()
    
    # Release The Lock
    
    self.cv.release()
    
# Create Consumer Class

class Consumer:
    def __init__(self, prod):
        self.prod = prod
        
    def consume(self):
        
        # Get Lock On Condition Object
        
        self.prod.cv.acquire()
        
        # Wait Only For 0 Seconds After The Production
        
        self.prod.cv.wait(timeout=0)
        
        # Release The Lock
        
        self.prod.cv.release()
        
        # Display The Contents Of List
        
        print(self.prod.lst)
        
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

 
     