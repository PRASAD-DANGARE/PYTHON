# Python Program To Pass Argument To A Function And Execute It Using A Thread

'''
Function Name    :  Pass Argument To A Function And Execute It Using A Thread
Function Date    :  3 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from threading import* # Create A Thread Without Using A Class

# Create A Function

def display(str):
    print(str)
    
# Create A Thread And Run The Function For 5 Times

for i in range(5):
    t = Thread(target=display, args=('Hello', )) 
    t.start()