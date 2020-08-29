# Python Program To Search For The Position Of An Elements In An Array Using Sequential Search / Linear Search

'''
Function Name    :  Sequential Search / Linear Search. 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from array import*

x = array('i', []) # Create An Empty Array To Store Integers

print('How Many Elements? : ', end= '') # Store Elements Into The Array x
n = int(input()) # Accept Input Into n

for i in range(n): # Repeat For n Times
    print('Enter Elements : ', end= '')
    x.append(int(input())) # Add The Elements To The Array x
    
print('Original Array : ', x)
print("\n")

print('Enter Elements To Search : ', end= '')
s  = int(input()) # Accept Elements To Be Search
print("\n")

# Linear Search / Sequential Search

flag = False # This Becomes True If The Elements Is Found

for i in range(len(x)): # Repeat i From 0 To no. Of Elements
    if s == x[i]:
        print('Found At Position = ', i + 1)
        flag = True
if flag == False:
    print('Not Found In The Array')
    