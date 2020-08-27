# python program to display even numbers between m and n (user through)

'''
Function Name    :  Even Numbers Between M and N
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

m , n = [int(i) for i in input("Enter Minimum And Maximum Range With A Space:").split(',')]
x = m # starts from m onwards
if x%2 != 0: # if x is not even 
    x = x + 1
while x >= m and x <= n :
    print(x)
    x += 2