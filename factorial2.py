# Python Program A Function To Check If A Number Is Prime Or Not

'''
Function Name    :  Function To Check A Number Is Prime Or Not. 
Function Date    :  4 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  String
'''

def prime(n):
    """ To Check If n Is Prime Or Not """
    
    x = 1 # This Will Be 0 If Not Prime
    for i in range(2, n): # Divide By Any Number
        if n % i == 0: # If Divisible By Any Number
            x = 0 # Take x As 0
            break
        else:
            x = 1 # else Take x As 1
    return x

# Test If A Number Is Prime Or Not

num = int(input('\n Enter Only One Number : '))
print("\n")

# Check If num Is Prime Or Not

result = prime(num)
if result == 1:
    print(num, 'Is Prime')
    print("\n")
else:
    print(num, 'Is Not Prime')
    print("\n")