# Python Program To Read Characters From A Text File

'''
Function Name    :  Read Characters From A Text File
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

f = open('myfile.txt', 'r')

# Read All Characters From File

str = f.read()

# Display Them On The Screen

print(str)

# Closing The File

f.close()

