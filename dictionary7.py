# Python Program To Accept A Dictionary And Display Its Elements

'''
Function Name    :  Accept A Dictionary And Display Its Elements.
Function Date    :  13 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

def fun(dictionary):
    for i, j in dictionary.items():
        print(i, '--', j)
        
# Take A Dictionary 

d = {'a': "Apple", 'b': "Book", 'c': "Cook"}

# Call The Function And Pass The Dictionary

fun(d)
