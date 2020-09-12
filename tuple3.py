# Python Program To Insert A New Elements Into A Tuple Of Elements At A Specified Position

'''
Function Name    :  Insert New Element Into Tuple At Any Position.
Function Date    :  12 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

print("\n")

names = (' Prasad', 'Hritik','Shubham', 'Shiva')
print(names)

# Accept New Name And Position Numbers

lst = [input('\n Enter A New Name : ')]
new = tuple(lst)
pos = int(input('\n Enter Position No : '))

# Copy From 0th To pos-2 Into Tuple names1

names1 = names[0:pos-1]

# Concatenate New Elements At pos -1

names1 = names1+new

# Concatenate The Remaining Elements Of Names From pos-1 Till End

names = names1+names[pos-1:]
print(names)
print("\n")