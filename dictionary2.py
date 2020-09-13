# Python Program To Retrieve Keys, Values And Key-Value Pairs From A Dictionary

'''
Function Name    :  Retrieve Keys, Value And Key-Value Pairs From Dictionary.
Function Date    :  13 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''


dict = {'Name' : 'Prasad', 'Id': 10, 'Salary': 100}

# Print Entire Dictionary

print(dict)

# Display Only Keys

print('Keys In dict = ', dict.keys())

# Display Only Values

print('Value In dict = ', dict.items())

# Display Both Key And Value Pairs As Tuples

print('Items In dict = ', dict.items())
