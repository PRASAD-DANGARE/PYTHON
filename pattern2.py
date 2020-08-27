# Python Program To Display Stars In Equilateral Triangle From Using Single Loop
'''
Function Name    :  Pattern Printing
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Pattern Name     :  Equilateral Triangle
'''

n = 40
for i in range(1, 11):
    print(' '*n, end= '') # Repeat Spaces For n Times.
    print('* '*(i)) # Repeat Star For i Times.
    n-=1