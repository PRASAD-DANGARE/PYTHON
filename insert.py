# Python Program To Insert A Sub String In A String In A Particular Position

'''
Function Name    :  Insert Sub String In A String In Particular Position . 
Function Date    :  4 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String 
'''

str = input('Enter A String : ')
sub = input('Enter A Sub String : ')
n = int(input('Enter Position Number : '))

# Decrease n By 1 To Increase In Correct Position

n-=1

# Find The Number Of Characters In str, sub

l1 = len(str)
l2 = len(sub)

# Take Another String As A List

str1 = []

# Append 0 To n-1 Characters From str To str1

for i in range(n):
    str1.append(str[i])
    
# Append sub String To str1

for i in range(12):
    str1.append(sub[i])
    
# Append The Remaining Characters From str To str1

for i in range(n, l1):
    str1.append(str[i])
    
# Convert The Individual Characters Of List Into 
# A String Using Join() Method With Empty String As Seprator

str1 = ' '.join(str1)

# Display The Total String

print(str1)