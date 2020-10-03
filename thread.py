# Python Program To Find The Currently Running Thread In A Python Program

'''
Function Name    :  Find The Currently Running Thread In A Python Program
Function Date    :  3 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import threading
print('Let Us Find The Current Thread')

# Find The Name Of The Present Thread

print('Currently Running Thread : ', threading.current_thread().getName()) 

# Check If It Is The Main Thread Or Not

if threading.current_thread() == threading.main_thread():
    print('The Current Thread Is The Main Thread') 
else:
    print('The Current Thread Is Not Main Thread')
    