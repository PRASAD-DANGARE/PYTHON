# Python Program To Sort The Array Elements Using Bubble Sort Technique.

'''
Function Name    :  Bubble Sort. 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from array import*


x = array('i', []) # Create An Empty Array To Store Integers

print('How Many Elements ? ', end='') # Store Elements Into Array x
n = int(input()) # Accept Input Into n

for i in range(n): # Repeat For n Times
    print('Enter Elements : ', end='')
    x.append(int(input())) # Add The Elements To The Array x
    
    
print('Original Array : ', x)
print("\n")

# Bubble Sort

flag = False # When Swapping Is Done , Flag Become True
for i in range(n-1): # i Is From 0 To n-1
    for j in range(n-1-i): # j Is From 0 To One Elements Lesser Than i
      if x[j] > x[j + 1]: # If 1st Elements Is Bigger Than The 2nd One
         t = x[j] # Swap j And j+1 Elements
         x[j] = x[j + 1]
         x[j + 1] = t
         flag = True # Swapping Done, Hence Flag Is True
    if flag == False: # No Swapping Means Array Is In Sorted Order
        break # Comes Out Of Inner For Loop
    else:
        flag = False # Assign Initial Value To Flag
            
print('Sorted Array = ', x)
