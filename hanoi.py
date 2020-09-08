# Python Program To Solve Tower Of Hanoi Problem

'''
Function Name    :  Tower Of Hanoi Logic. 
Function Date    :  8 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer  
'''

def towers(n, a, c, b):
    if n == 1:
# If Only 1 Disk , Then Move It From A To C
        
        print('Move Disk %i From Pole %s To Pole %s' %(n, a, c))
    else: # If More Than 1 Disk
        
# Move First n-1 Disk From A To B Using C As Intermidate Pole

        towers(n-1, a, b, c)    
        
# Move Remaining 1 Disk From A To C

        print('Move Disk %i From Pole %s To Pole %s' %(n, a, c))
        
# Move n-1 Disk From B To C Using A As Intermidate Pole

        towers(n-1, b, c, a)
        
# Call The Function

n = int(input('Enter NNumber Of Disks : '))

# We Should Change N Disk From A To C Using B As Intermidate Pole

towers(n, 'A', 'C', 'B')