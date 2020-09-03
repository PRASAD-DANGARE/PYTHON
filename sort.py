# Python Program To Sort A Group Of Strings Into Alphabetical Order

'''
Function Name    :  Sort A Group Of Strings Into Alphabetical Order. 
Function Date    :  3 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer,String
Output           :  String
'''

str = [] # Take An Empty Array

# Accept How Many Strings

n = int(input('How Many Strings ? '))
print("\n")

# Append String To str Array 

for i in range(n):
    print('Enter String : ', end= '')
    str.append(input())
    
    
# Sort The Array
# str.sort()

str1 = sorted(str)
print("\n")

# Display The Sorted Array

print('Sorted List : ')
for i in str1:
    print(i)
