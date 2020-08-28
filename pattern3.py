# Python Program To Display Numbers From 1 To 100 In Proper Format.

'''
Function Name    :  Pattern Printing
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Pattern Name     :  Display Numbers From 1 To 100
'''

for x in range(1, 11):
 for y in range(1, 11):
    print('{:8}'.format(x * y), end ='') # Each Column Size Is 8
 print()   