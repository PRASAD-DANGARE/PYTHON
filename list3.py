# Python Program To Find Common Elements In Two Lists

'''
Function Name    :  Find Comman Elements In Two List.
Function Date    :  10 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

# Take Two Lists

scholar1 = ['Prasad', 'Shubham', 'Hritik', 'Shiva']
scholar2 = ['Vishal', 'Shiva', 'Prasad', 'Sudarshan']

# Convert Them Into Sets

s1 = set(scholar1)
s2 = set(scholar2)

# Find Intersection Of Two Sets

s3 = s1.intersection(s2)

# Convert The Resultant Set Into A List

common = list(s3)

# Display The List

print(common)