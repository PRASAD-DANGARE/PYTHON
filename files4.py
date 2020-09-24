# Python Program To Read All The Strings From The Text File And Display Them

'''
Function Name    :  Read All The Strings From The Text File And Display Them
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

f = open('myfile.txt', 'r')

# Read Strings From The File

print('The File Contents Are : ')
str = f.read()
print(str)

# Closing The File

f.close()
