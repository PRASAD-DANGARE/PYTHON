# Python Program To Saerch For City Name In The File 
# And Display The Reords Numbers That Contains The City Name

'''
Function Name    :  Saerch For City Name In The File
Function Date    :  25 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

import os

reclen = 20 # Record Length As 20 Characters

# Find Size Of The Files

size = os.path.getsize('cities.bin')
print('Size Of File = {} Bytes'.format(size))

# Find Number Of Records In The File

n = int(size/reclen)
print('No. Of Records = {}'.format(n))

# Open The File In Binary Mode For Reading

with open('cities.bin', 'rb') as f:
    name = input('Enter City Name : ')
    
    # Convert Name Into Binary String
    
    name = name.encode()
    
    # Position Represents The Position Of File Pointer
    
    position = 0
    
    # Found Because True If City Is Found In The File
    
    found = False
    
# Repeat For N Records In The File

for i in range(n):
    
    # Place The File Pointer At Position
    
    f.seek(position)
    
    # Read 20 Characters
    
    str = f.read(20)
    
    # If Found
    
    if name in str:
        print('found at record no : ', (i+1))
        found = True
    
    # Go To The Next Record
    
    position += reclen
    
if not found:
    print('city not found')



    