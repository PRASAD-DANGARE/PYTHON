# Python Program To Evaluate Exponential Series

'''
Function Name    :  Evaluate Exponential Series
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Float
'''

x, n = [int(i) for i in input ("Enter Power Of e, no. Of Iteration : ").split(',')]

t = 1 # This Becomes First Term

sum = t # Till Now, Find The Sum Is 1 Only

print('Iteration= %d\tsum= %f' % (1,sum)) # Display Iteration No And Sum

# Repeat For 1nd To n-1th Terms

for j in range(1, n):
    t = t * x/j 
    
    # Find Next Term
    
    sum = sum + t; # Add It To Sum.
    print('iteration= %d\tsum= %f' % (j+1, sum))
