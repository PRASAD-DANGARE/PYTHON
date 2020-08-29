# Python Program To Understand Various Methods Of Array Class

'''
Function Name    :  Methods Of Array Class. 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from array import*

# 1) Create An Array With int Value

arr = array('i', [10,20,30,40,50])
print('Original Array : ', arr)
print("Next\n")

# 2) Append 30 To The Array arr , Adding Element X At End Of The Array

arr.append(30)
arr.append(60)
print('After Appending 30 And 60 : ', arr)
print("Next\n")

# 3) Insert 99 At Position Number 1st In arr

arr.insert(1, 99)
print('After Inserting 99 In 1st Position : ', arr)
print("Next\n")

# 4) Remove An Elements From arr

arr.remove(20)
print('After Removing 20 : ', arr)
print("Next\n")

# 5) Remove Last Element Using pop() Method

n = arr.pop()
print('Array After Using pop() : ', arr)
print('Popped Elements : ', n)
print("Next\n")

# 6) Finding Position Of Elements Using Index() Method

n = arr.index(30)
print('First Occurrence Of Elements 30 Is At : ', arr)
print("Next\n")

# 7) Convert An Array Into A List Using tolist() Method

lst = arr.tolist()
print('List : ', lst)
print('Array : ', arr) 
print("Last\n")