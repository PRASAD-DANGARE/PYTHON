# Python Program That Returns Even Numbers From A List

'''
Function Name    :  Returns Even Number From A List Using Lambda. 
Function Date    :  8 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

lst = [10,23,45,46,70,99]
lst1 = list(filter(lambda x: (x % 2 == 0), lst))
print(lst1)
