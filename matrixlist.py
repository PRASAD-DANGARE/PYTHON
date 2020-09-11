# Python Program To Retrieve Elements From A Matrix And Display Them
# Take A Nested List

'''
Function Name    :  Retrieve Elements From Matrix And Display.
Function Date    :  11 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer,String
Output           :  Integer,String
'''

mat = [[1,2,3], [4,5,6], [7,8,9]]

print('\n Display The List As It Is : ')
print(mat)

print('\n Display Row By Row : ')
for r in mat:
    print(r)
    

print('\n Display Each Column In Row 0 : ')
for c in mat[0]:
    print('%d' %c, end='')
print()

print('\n Display Each Column In Row 1 : ')
for c in mat[1]:
    print('%d' %c, end='')
print()

print('\n Display Each Column In Row 2 : ')
for c in mat[2]:
    print('%d' %c, end='')
print()

print('\n Display All Elements Using For : ')
for r in mat:
    for c in r: # Display Columns In Each Row
        print(c, end=' ')
    print()

print('\n Display All Elements Using For : ')
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print('%d' %mat[i][j], end='')
    print()
    
 