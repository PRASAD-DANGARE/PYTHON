# Python Program To Generate Fibonacci Number Series

'''
Function Name    :  Generate Fibonacci Series
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

n = int(input('How Many Fibonacci Numbers You Want? '))
f1 = 0 # First Fibonacci No
f2 = 1 # Second One
c = 2 # Count The No Of Fibonacci

if n == 1:
    print(f1)
elif n == 2:
    print(f1, '\n', f2, sep ='')
else:
    print(f1, '\n', f2, sep ='')
    while c<n:
        f = f1 + f2 # Add 2 And Get New 1
        print(f)
        f1, f2 = f2, f # Same As f1 = f2 , f2 = f
        c += 1 # Increment Counter
        
'''
Logic To Generate Fibonacci Numbers

F1 F2 F
0  1  2  3  4  5  6  7  8
   F1 F2 F
   
F1 = F2
F2 = F
F = F1 + F2
'''