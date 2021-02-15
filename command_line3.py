'''
Description      :  Addition In Command Line Arguments 
Function Date    :  15 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''


import sys

print("Demonstration Of Command Line Arguments")
print("Application Name" + sys.argv[0])

x = int(sys.argv[1])
y = int(sys.argv[2])

z = x + y
print(z)
