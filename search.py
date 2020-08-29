# Python Program To Search For The Position Of An Elements In An Array Using Index() Method

from array import*

x = array('i', []) # Create An Empty Array To Search Integers

print('How Many Elements? ', end= '') # Store Elements Into The Array x
n = int(input()) # Accept Input Into n

for i in range(n): # Repeat For n Times
    print('Enter Elements : ', end= '')
    x.append(int(input())) # Add The Elements To The Array x
    
print('Original Array : ', x)
print("\n")


print('Enter Elements To Search : ', end= '')
s = int(input()) # Accept Elements To Be Searched
print("\n")


# Index() Method Gives The Location Of The Elements In The Array 
try :
    pos = x.index(s)
    print('Found At Position = ', pos + 1)
    
except ValueError : # If Elements Not Found Then ValueError Will Rise 
    print('Not Found In The Array ')
    