# Python Program To Show Dead Lock Of Threads Due To Locks On Objects

'''
Function Name    :  Show Dead Lock Of Threads Due To Locks On Objects
Function Date    :  5 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''


from threading import*

# Take Two Locks

l1 = Lock()
l2 = Lock()

# Create A Function For Booking A Ticket

def bookticket():
    l1.acquire()
    print('Bookticket Locked Trains')
    print('Bookticket Wants To Lock On Compartment')
    l2.acquire()
    print('Bookticket Locked Compartment')
    l2.release()
    l1.release()
    print('Booking Ticket Done...')
    
# Create A Function For Cancelling A Ticket

def cancelticket():
    l2.acquire()
    print('cancelticket Locked Compartment')
    print('cancelticket Wants To Lock On Train')
    l2.acquire()
    print('cancelticket Locked Train')
    l1.release()
    l2.release()
    print('Cancellation Of Ticket Is Done...')
    
# Create Two Threads And Run Them

t1 = Thread(target=bookticket)
t2 = Thread(target=cancelticket)

t1.start()
t2.start()



