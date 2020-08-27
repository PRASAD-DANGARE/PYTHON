# Python Program To Add Two Numbers Using Arguments Parser(Integer,Float)
'''
Function Name    :  Calculate Sum Of Two Numbers Using Argument Parser
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer,Float
Output           :  Float
'''
from argparse import ArgumentParser

# Create Argument Parser Class Object

parser = ArgumentParser(description="This Program Calculate The Sum Of Two Numbers:")

# Add Two Arguments With The Name n1 And n2 And Type As Float

parser.add_argument("n1", type=float, help="input first number")
parser.add_argument("n2",type=float, help="input second number")

# Retrive The Arguments Passed To Program

args = parser.parse_args()

# Convert The n1 And n2 Value Into Float Type Then Add Them

result = float(args.n1)+float(args.n2)
print("Sum Of Two Numbers Are =", result)

