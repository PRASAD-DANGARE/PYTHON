# Python Program To Calculate Cosine Value Of Given Angle In Degrees By Evaluating Cosine Series.

'''
Function Name    :  Calculate Cosine Value Of Angle Into Degrees Using Cosine Series
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Float
'''

x, n = [int(i) for i in input ("Enter Angle Value, Number Of Iteration : ").split(',')]

r = (x * 3.14159)/180 # Convert Angle From Degrees Into Radious

t = 1 # This Becomes First Term

sum = 1 # Till Now, Find The Sum Is 1 Only

print('Iteration= %d\tsum= %f' % (1,sum)) # Display Iteration No And Sum

i = 1 # Denominator For Second Term

# Repeat For 2nd To nth Terms

for j in range(2, n + 1):
    t = (-1)*t*r**2/(i*(i + 1))
    
    # Find Next Term
    
    sum = sum + t; # Add It To Sum.
    print('iteration= %d\tsum= %f' % (j, sum))
    i += 2 # Increase i Value By 2 For Denominator For Next Term