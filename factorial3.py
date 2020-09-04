# Python Program That Generates Prime Number With The Help Of A Function To Test Prime Or Not

'''
Function Name    :  Function To Test Whether Number Is Prime Or Not. 
Function Date    :  4 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  String
'''

def prime(n):
    """ to check if n is prime or not """
    
    x = 1 # This Will Be 0 If Not Prime 
    for i in range(2, n):
        if n % i == 0:
            x = 0
            break
        else:
            x = 1
    return x


# Generate Prime Number Series

num = int(input('How Many Primes Do You Want ? '))

i = 2 # Start With i Value 2
c = 1 # This Counts The Number Of Primes

while True: # If I Is Prime, Display It
    if prime(i): # If I Is Prime, Display It
        print(i)
        c += 1 # Increase Counter
    i += 1 # Generate Next Number To Test
    if c > num: # If Count Exceeds num
        break # Come Out Of While-Loop