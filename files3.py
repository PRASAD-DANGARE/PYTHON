# Python Program To Store A Group Of Strings Into A Text File

'''
Function Name    :  Store A Group Of Strings Into A Text File myfile.txt
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from ast import Str


f = open('myfile.txt', 'w')

# Enter Strings From Keyboard

print('Enter Text (@ at end) : ')
while Str != '@':
    str = input()
    
    # Write The String Into File
    
    if(str != '@'):
        f.write(str+"\n")
        
# Closing The File

f.close()