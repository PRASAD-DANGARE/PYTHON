# Python Program To Understand The Effects Of An Exception


'''
Function Name    :  Effects Of An Exception
Function Date    :  22 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

# Open File

f = open("myfile", "w")

# Do Some Processing On The File
# Accepts a, b Values, Store The Result Of a/b Into The File

a, b = [int(x) for x in input("\n Enter two numbers With Space: ").split()]
c = a/b
f.write("Writing %d Into myfile" %c)

# Close The File

f.close()
print('File Closed')
print("\n")


