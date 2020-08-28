# Python Program To Create One Array From Another Array

'''
Function Name    :  Create One Array From Another Array
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Float
Output           :  Float
'''

from array import*

arr1 = array('d', [1.5,2.5,-3.5,4])
arr2 = array(arr1.typecode,[a*3 for a in arr1])
print('The arr2 Elements Are : ')
for i in arr2 : print(i)
