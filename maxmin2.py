# Python Program To Know How Many Times An Elements Occured In The List

'''
Function Name    :  How Many Times An Element Occured In A List.
Function Date    :  10 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

x = [] # An Empty List

n = int(input('\n How Many Elements ? ')) # Accept Input Into n

for i in range(n): # Repeat For n Times
    print('Enter Elements : ', end='')
    x.append(int(input())) # Add The Elements To The List x
    
print('The List Is : ', x) # Display The List


y = int(input('\n Enter Elements To Count : '))
c = 0
for i in x:
    if(y==i): c+=1
print('\n {} Is Found {} Times . '.format(y, c))
print("\n")
