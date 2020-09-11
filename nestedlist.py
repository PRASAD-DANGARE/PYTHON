# Python Program To Create Nested List And Display Its Elements
# Create List With Another List As Elements

'''
Function Name    :  Create Nested List And Display Its Elements.
Function Date    :  11 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer,String
Output           :  Integer,String
'''


list = [10,20,30, [50, 60]]
print('Total List = ', list) # Display Entire List
print('First Elements= ', list[0]) # Display First Elements

print('Last Elements Is Nested List = ', list[3]) # Display Nested List
for x in list[3]: # Display All Elements In Nested List
    print(x)