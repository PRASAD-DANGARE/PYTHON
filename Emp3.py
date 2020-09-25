# Python Program To Unpickel Emp Class Objects

'''
Function Name    :  Unpickel Emp Class Objects
Function Date    :  25 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

import Emp, pickle

# Open The File To Read Objects

f = open('emp.dat', 'rb')

print('Employees Details : ')
while True:
    try:
        # Read Objects From File f
        
        obj = pickle.load(f)
        
        # Display The Contents Of Employee obj
        
        obj.display()
        
    except EOFError:
        
        print('end of file reached...')
        break
    
    # Close The File
    
    f.close()
    

