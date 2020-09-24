# Python Program To Append Data To An Existing File And Then Displaying The Entire File

'''
Function Name    :  Append Data To An Existing File & Then Display Entire File
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

f = open('myfile.txt', 'a+')

print('Enter Text To Append(@ at end) : ')

while str != '@':
    str = input() # Accept String Into str
    
    # Write The String Into File
    
    if (str != '@'):
        f.write(str+"\n")
        
# Put The Files Pointer To The Beginning Of File

f.seek(0,0)

# Read Strings From The File

print('The File Contents Are : ')
str = f.read()
print(str)

# Closing The File

f.close()
