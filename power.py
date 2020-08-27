# Python Program To Find The Power Value Of Number When It Is Raised To A Particular Power.

'''
Function Name    :  Power Value Of A Number
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Float
'''

import argparse
from argparse import ArgumentParser



# Call The Argument Parser().

parser = argparse.ArgumentParser()

# Add The Arguments To The Parser.

parser.add_argument('nums', nargs=2) # We Can Specify Number Of Arguments In The Add_Argument() Method Using nargs Attribute.

# Retrive The Arguments Into args Object.

args = parser.parse_args()

# Find The Power Value , args.nums Represent A List.

print('Number =', args.nums[0])
print('Its Power =', args.nums[1])

# Convert The Argument Into Float And Find The Power.

result = float(args.nums[0])**float(args.nums[1])
print('result =', result)
