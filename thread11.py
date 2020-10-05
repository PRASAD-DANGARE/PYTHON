# Python Program With Good Logic To Avoid Deadlocks

'''
Function Name    :  Good Logic To Avoid Deadlocks
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
    print('Bookticket Locked Train')
    print('Bookticket Wants To Lock On Compartment')
    l2.acquire()
    print('Bookticket Locked Compartment')
    l2.release()
    l1.release()
    print('Booking Ticket Done...')
    
# Create A Function For calling A Ticket

def cancelticket():
    l1.acquire()
    print('Cancelticket Locked Compartment')
    print('Cancelticket Wants To Lock On Train')
    l2.acquire()
    print('Cancelticket Locked Train')
    l2.release()
    l1.release()
    print('Cancellation Of Ticket Is Done...')
    
# Create Two Threads And Run Them

t1 = Thread(target=bookticket)
t2 = Thread(target=cancelticket)

t1.start()
t2.start()