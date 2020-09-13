# Python Program To Create A Dictionary From Keyboard And Display The Elements

'''
Function Name    :  Create Dictionary From Keyboard And Display Elements.
Function Date    :  13 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

x = {} # Take Empty Dictionary

print('\n How Many Elements ? ', end='')
n = int(input()) # n Indicates Numbers Of Key-Value Pairs

for i in range(n):
    print('Enter Key : ', end='')
    k = input() # Key Is String
    print('Enter Its Value : ', end='')
    v = int(input())
    x.update({k:v})
    
# Dislay The Dictionary

print('\n The Dictionary is : ', x)
print("\n")