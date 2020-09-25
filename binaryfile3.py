# Python Program To Update Or Modify A Record In A Binary File

'''
Function Name    :  Update Or Modify A Record In A Binary File
Function Date    :  25 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

import os

# Take Record Length As 20 Characters

reclen = 20

# Find Size Of The Files

size = os.path.getsize('cities.bin')
print('Size Of File = {} Bytes'.format(size))

# Find Number Of Records In The File

n = int(size/reclen)
print('No. Of Records = {}'.format(n))

# Open Files In Binary Mode For Reading

with open('cities.bin', 'r+b') as f:
    name = input('Enter City Name : ')
    
    # Convert Name Into Binary String
    
    name = name.encode()
    
    newname = input('Enter New Name : ')
    
    # Find Length Of Newname
    
    ln = len(newname)
    
    # Add Spaces To Make Its Length To Be 20
    
    newname = newname+ (20-ln)*' '
    
    # Convert Newname Into Binary String
    
    newname = newname.encode()
    
    # Position Represents The Position Of File Pointer
    
    position = 0
    
    # Found Becomes True If City Is Found In The File
    
    found = False
    
    # Repeat For n Records In The File
    
    for i in range(n):
        
        # Place The File Pointer At PAosition
        
        f.seek(position)
        
        # Read 20 Characters
        
        str = f.read(20)
        
        # If Found
        
        if name in str:
            print('Updated Record No : ', (i+1))
            found=True
            
            # Go Back 20 Bytes From Current Position
            
            f.seek(-20, 1)
            
            # Update The Record
            
            position+=reclen
            
    if not found:
        print('City Not Found')
        