# Python Programs To Retrieve The Elements From 3-D Array

'''
Function Name    :  Retrieve The Elements From 3-D Array . 
Function Date    :  31 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

# Create A 3-D Array With Size 2x2x3

a = [[[1,2,3],
      [4,5,6]],
     
     [[7,8,9],
      [10,11,12]]]

# Display Elements By Elements

for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i] [j])):
            print(a[i] [j] [k], end = '\t')
        print()
    print()
    
      
      