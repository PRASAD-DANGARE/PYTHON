# Python Program To Find Maximum And Minimum Elements In A List Of Elements

'''
Function Name    :  Find Maximum And Minimum Elements In A List.
Function Date    :  10 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

x = [] # An Empty List

print('\n how many elements ? ', end='')
n = int(input()) # Accept Input Into n

for i in range(n): # Repeat For n Times
    print('enter elements : ', end='')
    x.append(int(input())) # Add The Elements To The List x
    
print('the list is : ', x) # Display The List
print("\n")

big = x[0] # Initially oth Element Becomes Maximum And Minimum
small = x[0]

for i in range(1, n): # Repeat From 1 To n-1 Elements
    if x[i] > big: big = x[i] # If Any Other Elements Is > Big , Take It As Big
    if x[i] < small: small = x[i] # If Any Other Elements Is < Small Take It As Small
    
print('maximum is : ', big) # Display Max And Min Elements
print('minimum is : ', small)
print("\n")
 