# Python Program To Search For The Position Of A String In A Given Group Of Strings

str = [] # Take An Empty Array

# Accept How Many Strings

n = int(input('How Many Strings ? '))
print("\n")

# Append Strings To str Array

for i in range(n):
    print('Enter Strings: ', end= '')
    str.append(input())
    
# Ask For The String To Search

print("\n")

s = input('Enter String TO Be Search : ')
print("\n")

# Linear Search Or Sequential Search

flag = False

for i in range(len(str)):
    if s == str[i]:
        print('Found At : ', i + 1)
        flag = True
        
if flag == False:
    print('Not Found')