# Python Program To Create A Dictionary And Find The Sum Of Values

'''
Function Name    :  Create Dictionary And Find The Sum Of Values.
Function Date    :  13 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

dict = eval(input("Enter Elements In {} : "))

# Find The Sum Of Values

s = sum(dict.values())
print('Sum Of Values In The Dictionary : ', s) # display sum
