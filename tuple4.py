# Python Program To Modify Or Replace An Existing Element Of A Tuple With A New Elements

'''
Function Name    :  Modify, Replace Element Of A Tuple With New Element.
Function Date    :  12 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

num = (10, 20, 30, 40, 50)
print(num)

# Accept New Elements And Position Number

lst = [int(input('\n Enter A New Elements : '))]
new = tuple(lst)
pos = int(input('\n Enter Position No : '))

# Copy From 0th To pos-2 Into Another Tuple num1

num1 = num[0:pos-1]

# Concatenate New Elements At pos -1

num1 = num1+new

# Concenate The Remaining Elements Of num From Pos Till End

num = num1+num[pos:]
print(num)
print("\n")