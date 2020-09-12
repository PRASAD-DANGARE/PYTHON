# Python Program To Delete An Element From A Particular Position In The Tuple

'''
Function Name    :  Delete An Element From A Particular Position.
Function Date    :  12 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

print("\n")

num = (10,20,30,40,50)
print(num)

# Accept Position Number Of The Elements To Delete

pos = int(input('\n Enter Position To Delete : '))

# Copy From 0th To pos-2 Into Another Tuple num1

num1 = num[0:pos-1]

# Concatenate The Remaining Elements Of num From pos Till End

num = num1+num[pos:]
print(num)
print("\n")

