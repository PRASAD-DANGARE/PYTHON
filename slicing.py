# Python Program To Understand Slicing Operations On Array

'''
Function Name    :  Slicing Operations On Array. 
Function Date    :  31 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

a = arange(10, 16) # Create Array a With Elements 10 To 15.
print(a)
print("\n")


b = a[1:6:2] # Retrieve From 1st To One Elements Prior To 6th Elements In Steps Of 2
print(b)
print("Next \n")


b = a[::] # Retrieve All Elements From a
print(b)
print("Next \n")


b = a[-2:2:-1] # Retrieve From 6-2 = 4 To One Elements Prior To 2nd Elements In Descreasing Step Size
print(b)
print("Next \n")


b = a[:-2:] # Retrieve From 0th To One Elements Prior To 4th Elements (6-2 = 4th)
print(b)
print("Last \n")