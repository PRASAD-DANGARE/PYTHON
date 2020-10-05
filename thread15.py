# Python Program To Understand The Creation Of Daemon Thread

'''
Function Name    :  Creation Of Daemon Thread
Function Date    :  5 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from threading import*
from time import*

# To Display Date And Time Once In Every 2 Seconds

def display():
    for i in range(5):
        print('Normal Thread : ', end='')
        print(i+1)
        sleep(1)
        
# To Display Date And Time Once In 2 Seconds

def display_time():
    while True:
        print('Daemon Thread : ', end='')
        print(ctime())
        sleep(2)
        
# Create A Normal Thread And Attach It To Display() And Run It

t = Thread(target=display)
t.start()

# Create Another Thread And Attach It To Display_time()

d = Thread(target=display_time)

# Make The Thread Daemon

d.daemon = True

# Run The Daemon Thread

d.start()

        