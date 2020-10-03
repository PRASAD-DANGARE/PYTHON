# Python Program To Create A Thread And Use It To Run A Function

'''
Function Name    :  Create A Thread And Use It To Run A Function
Function Date    :  3 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from threading import* # Create A Thread Without A Class

# Create A Function

def display():
    print('Hello Im Prasad') 
    
# Create A Thread And Run The Function As Its Target

for i in range(5):
    
    # Create The Thread And Specify The Function As Its Target
    
    t = Thread(target=display)
    
    # Run The Thread
    
    t.start()