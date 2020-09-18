# Python Program To Use The Student Class Which Is Already Available In student.py

'''
Function Name    :  Using Student Class student.py In This Program student2.py
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

# Save This Program student2.py
# Using Student Class

from student import student

# Create Instance

s = student()

# Store Data Into The Instance

s.setid(100)
s.setname('Prasad')
s.setaddress('Sanjuda Complex, Papadewasti, 412308, Pune')
s.setmarks(970)

# Retrieve Data From Instance And Display

print('\n Id = ', s.getid()) 
print('Name = ', s.getname())
print('Address = ', s.getaddress())
print('Marks = ', s.getmarks())
print("\n")
