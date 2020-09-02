# Python Program To Understand The Concept Of Immutable Objects (String)
# It Helps The Programmer To Know SomeBody Is Modifing There Code Which Is Not Possible In Case Of Immutabel Objects

str = 'prasad'
print(str[0]) # Display p

str[0] = 'x'

'''
So It Is Not Possible To Change The Value

TraceBack (Most Recent Call Last):
     File "immutable.py", Line 7, In <Module>
     str[0] = 'x'
TypeError : 'str' Object Does Not Support Item Assignment
'''

