# Python Program To Calculate Sine Value Of Given Angle In Degrees By Evaluating Sine Series.

'''
Function Name    :  Calculate Sine Value Of Angle Into Degrees Using Sine Series
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Float
'''

x, n = [int(i) for i in input ("Enter Angle Value, Number Of Iteration : ").split(',')]

r = (x * 3.14159)/180 # Convert Angle From Degrees Into Radious

t = r # This Becomes First Term

sum = r # Till Now, Find The Sum

print('Iteration= %d\tsum= %f' % (1,sum)) # Display Iteration No And Sum

i = 2 # Denominator For Second Term

# Repeat For 2nd To nth Terms

for j in range(2, n + 1):
    t = (-1)*t*r*r/(i*(i + 1))
    
    # Find Next Term
    
    sum = sum + t; # Add It To Sum.
    print('iteration= %d\tsum= %f' % (j, sum))
    i += 2 # Increase i Value By 2 For Denominator For Next Term