# Python Program Where Two Threads Are Acting On The Same Method To Allot A Berth For The Passenger


'''
Function Name    :  Two Threads Are Acting On The Same Method 
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
        
    # A Method That Reserves Berth
    
    def reserve(self, wanted):
        
        # Display No. Of Available Berths
        
        print('Available no. of berths = ', self.available)
        
        # If Available >= Wanted , Allot The Berth
        
        if(self.available >= wanted):
            
            # Find The Thread Name
            
            name = current_thread().getName()
            
            # Display Berth Is Allocated For The Person
            
            print('%d berths allotted for %s' %(wanted, name))
            
            # Make Time Delay So That The Ticket Is Printed 
            
            sleep(1.5)
            
            # Decrease The No. Of Available Berths
            
            self.available -= wanted
        
        else:
            
            # If Available < Wanted Then Say Sorry
            
            print('Sorry , No Berths To Allot')
            
# Create Instance To Railway Class
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