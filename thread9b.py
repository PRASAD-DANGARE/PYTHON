# Python Program Acheiving Thread Synchronization Using Locks

'''
Function Name    :  Acheiving Thread Synchronization Using Locks
Function Date    :  5 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''


from threading import*
from time import*

class Railway:
    
    # Constructor That Accepts No Of Available Berths
    
    def __init__(self, available):
        self.available = available
        
        # Create A Lock Object
        
        self.l = Lock()
        
    # A Method That Reserve Berth
    
    def reserve(self, wanted):
        
        # Lock The Current Object
        
        self.l.acquire()
        
        # Display No. Of Available Births
        
        print('Available No. Of berths = ', self.available)
        
        # if available >= Wanted , Allot The Berth
        
        if(self.available >= wanted):
            
            # Find The Thread Name
            
            name = current_thread().getName()
            
            # Display Berth Is Allotted For The Person
            
            print('%d Berth Alloted For %s' %(wanted, name))
            
            # Make Time Delay So That The Ticket Is Priented
            
            sleep(1.5)
            
            # Decrease The No Of Available Berths
            
            self.available -= wanted
        else:
            
            # If Available < Wanted , Then Say Sorry
            
            print('Sorry , No Berth To Allot')
            
        # Task Is Completed , Release The Lock
        
        self.l.release()
        
# Create Instance To RailwayClass
# Specify Only Berth Is Available

obj = Railway(1)

# Create Two Thread And Specify 1 Berth Is Needed

t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))

# Give Names To The Thread

t1.setName('First Person')
t2.setName('Second Person')

# Run The Thread

t1.start()
t2.start()
            