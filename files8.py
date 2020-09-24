# Python Program To Copy An Image Into Another Files

'''
Function Name    :  Copy An Image Into Another Files
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  --
Output           :  --
'''

# Open The File In Binary Modes

f1 = open('new.jpg.png', 'rb')
f2 = open('neww.jpg.jpg', 'wb')

# Read Bytes From f1 And Write Into f2

bytes = f1.read()
f2.write(bytes)

# Close The File

f1.close()
f2.close()

