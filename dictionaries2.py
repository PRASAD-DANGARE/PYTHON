# Python Program To Find The Number Of Occurrence Of Each Letter In A String

'''
Function Name    :  Number Of Occurrence Of Each Letter In String.
Function Date    :  13 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

str = "Book"

# Take An empty dictionaries

dict = {}

# Store Into dict Each Letter As Key And Its
# Numbers Of Occurrence As Value

for x in str:
    dict[x] = dict.get(x, 0) + 1
    
# Display Key And Values Pairs Of dict

for k, v in dict.items():
    print('Key - {}\t Its Occurrence = {} '.format(k, v))
    