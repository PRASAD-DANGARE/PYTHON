# Find Square Of A Given Number 
# Argument Parser provides help and tells the user how to use the program through command line.
'''
Function Name    :  Square Root Of Given Number Using Argument Parser
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

import argparse


# create argument parser class object

parser = argparse.ArgumentParser(description ="This Program Display The Square Value Of Given Number")

# Add One Argument With Name num And Type As Integer

parser.add_argument("num", type=int, help="Please Input Integer Type Number")

# Retrive The Argument Passed To Program

args = parser.parse_args()

# Find The Square Of Argument Passed 

result = args.num**2
print("Square Value = ", result)

'''
Cases To Be Happen :

1) If User Type 5.5 In Input So It Display arg.py: error : Argument num: Invalid int Value 5.5.

2) If User Type 2 Numbers 5, 15 It Display arg.py: error : The Following Argument Are Required : num.

3) If User Does Not Type Any Argument It Display arg.py : error : The Following Argument Are Required : num.

4) If User Wants Help Then Type -h It Display This Program , Display The Square Value Of Given Number Position Arguments:
   num Please Input Integer Type Number Optional Arguments: -h, --help Show This Help Message Or Exit.
'''
   
