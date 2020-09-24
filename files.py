# Python Program To Create A Text File To Store Individual Characters

'''
Function Name    :  Create A Text File To Store Individual Characters
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

# Open The File For Writing Data

f = open('myfile.txt', 'w')

# Enter Characters From Keyboard

str = input('Enter Text : ')

# Write The String Into File

f.write(str)

# Closing The File

f.close()


