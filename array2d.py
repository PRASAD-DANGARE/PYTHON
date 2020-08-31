# Python Program To Retrieve The Elements From A 2-D Array Using Indexing

'''
Function Name    :  Retrieve The Elements From 2-D Array . 
Function Date    :  31 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

a = [[1,2,3], [4,5,6], [7,8,9]] # Create A 2-D Array With 3 Rows And 3 Columns

for i in range(len(a)): # Display Only Rows
    print(a[i])
    
    
for i in range(len(a)): # Display Elements By Elements
    for j in range(len(a[i])):
        print(a[i] [j], end = ' ')
        
        
 