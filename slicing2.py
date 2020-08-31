# Python Program To Retrieve And Display Elements Of A Numpy Array Using Indexing

'''
Function Name    :  Retrieve And Display Elements Using Indexing. 
Function Date    :  31 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

a = arange(10, 16) # Create Array a With Elements 10 To 15.
print(a)
print("\n")


a = a[1:6:2] # Retrieve From 1st To One Elements Prior To 6th Elements In Steps Of 2
print(a)
print("Next \n")

# Display Elements Using Indexing

i = 0
while (i < len(a)):
    print(a[i])
    i += 1
  