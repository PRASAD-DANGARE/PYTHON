# Python Program To Know Whether A Sub String Exists In Main String Or Not

'''
Function Name    :  Whether A Sub String Exists In Main String Or Not. 
Function Date    :  1 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

str = input('Enter Main String : ')
print("\n")

sub = input('Enter Sub String : ')
print("\n")


if sub in str:
    print(sub + 'Is Found In Main String')
    print("\n")
else:
    print(sub + 'Is Not Found In The Main String') 
    print("\n")