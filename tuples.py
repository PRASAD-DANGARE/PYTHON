# Python Program To Find The First Occurrence Of An Elements In A Tuple

'''
Function Name    :  First Occurance Of An Elements In A Tuple.
Function Date    :  11 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

str = input('\n Enter Elements Seperated By Commas : ').split(',')

lst = [int(num) for num in str]

tup = tuple(lst)

print('\n The Tuple Is : ', tup)

ele = int(input('\n Enter An Elements To Search : '))
try:
    pos = tup.index(ele)
    print('\n Elements Position No : ', pos + 1)
    
except ValueError:
    print('\n Elements Not Found In Tuple')
    print("\n")
    
    