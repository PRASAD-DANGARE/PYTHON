# Python Program To Find The First Occurance Of Sub String In A Given Main String

'''
Function Name    :  Check The First Occurance Of Sub String In A Given Main String . 
Function Date    :  1 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  Integer
'''

str = input('Enter Main String : ')
print("\n")

sub = input('Enter Sub String : ')
print("\n")


# Find Position Of Sub In str
# Search From 0th To Least Characters In str

n = str.find(sub, 0, len(str))

# Find() Returns -1 If Sub String Is Not Found


if n == -1:
    print('Sub String Not Found')
    print("\n")
else:
    print('Sub String Found At Position : ', n+1)
    print("\n") 