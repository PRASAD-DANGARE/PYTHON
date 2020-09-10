# Python Program To Create Lists Using range() Function

'''
Function Name    :  Create List Using range() Function.
Function Date    :  10 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

list1 = range(10) # Display Elements By Elements
for i in list1:
    print(i,', ', end='')
print() # Throw Cursor To Next Line

# Create List With Integer From 5 To 9

list2 = range(5, 10)
for i in list2:
    print(i,', ', end='')
print()

# Create A List With Odd Numbers From 5 To 9

list3 = range(5, 10, 2)
for i in list3:
    print(i,', ', end='')
     