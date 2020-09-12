# Python Program To Sort A Tuple With Nested Tuples

'''
Function Name    :  Sort A Tuple With Nested Tuples.
Function Date    :  12 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

# Take Employee Tuple With Id Number, Name And Salary
emp = ((10, "Prasad", 1234.01), (20, "Shubham", 5678.02), (30, "Hritik", 9101112.03), (40, "Shiva", 13141516.04))
print("\n")

print(sorted(emp)) # Sort By Default On Id
print("\n")
 
print(sorted(emp, reverse=True)) # Reverses On Id
print("\n")

print(sorted(emp, key=lambda x: x[1])) # Sort On Name
print("\n")

print(sorted(emp, key=lambda x: x[2])) # Sort On Salary
print("\n")