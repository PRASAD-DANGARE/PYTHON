# Python Program Where Producer And Consumer Thread Communicate With Each Other Through A Boolean Type Variable

'''
Function Name    :  Producer And Consumer Thread Communicate With Each Other
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
        self.dataprodover=False
        
    def produce(self):
        
        # Create 1 To 10 Items And Add To The List
        
        for i in range(1, 11):
            self.lst.append(i)
            sleep(1)
            print('Item Produced...')
            
        # Inform The Consumer That The Data Production Is Completed
        
        self.dataprodover=True
        
# Create Consumer Class

class Consumer:
    def __init__(self, prod):
        self.prod = prod
        
    def consume(self):
        
        # Sleep For 100 Ms As Long As DataProdover Is False
        
        while self.prod.dataprodover==False:
            sleep(0.1)
            
        # Display The Content Of List When Data Production Is Over
        
        print(self.prod.lst)
        
# Create Producer Object

p = Producer()

# Create Consumer Object And Pass Threads

c = Consumer(p)

# Create Producer And Consumer Threads

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume) 

# Run The Threads

t1.start()
t2.start() 
