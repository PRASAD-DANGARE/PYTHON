# Python Programs To Accept And Display A Group Of Numbers

'''
Function Name    :  Accept And Display Group Of Numbers . 
Function Date    :  2 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer 
'''

str = input('Enter Numbers Seprated By Space : ')
print("\n")

# Cut The String Where A Space Is Found

lst = str.split(' ')

# Display The Number From The List

for i in lst:
    print(i)