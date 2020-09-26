# Python Program To Use mmap And Performing Various Operations On A Binary File

'''
Function Name    :  Use mmap And Performing Various Operations On A Binary File
Function Date    :  26 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

import mmap, sys
from os import name

# Display A Menu

print('1 To Display All Entries :')
print('2 To Display Phone Number :')
print('3 To Modify An Entry :')
print('4 Exit :')

ch = input('\n Your Choice : ')
if ch=='4':
    sys.exit()
    
with open("phonebook.dat", "r+b") as f:
    
    mm = mmap.mmap(f.fileno(), 0) # Memory-map The File, Size 0 Means Whole File
    
    # Display The Entire File
    
    if(ch == '1'):
        print(mm.read().decode())
        
    # Display Phone Number
    
    if(ch =='2'):
        name = input('\n Enter Name : ')
        n = mm.find(name.encode()) # Find Position Of Name
        n1 = n+len(name) # Go To End Of Name
        
        # Display The Next 10 Bytes
        
        ph = mm[n1: n1+10]
        print('\n Phone No : ', ph.decode())
        
    # Modify Phone Number
    
    if(ch == '3'):
        name = input('\n Enter Name : ')
        n = mm.find(name.encode()) # Find The Position Of Name
        n1 = n+len(name) # Go To End Of Name
        
        # Enter New Phone Number
        
        ph1 = input('\n Enter New Phone Number : ')
        mm[n1: n1+10] = ph1.encode() # The Old Phone Number Is 10 Bytes After n1
        
    # Close The map
    
    mm.close()
    