# Python Program To Find The Product Of Elements Of Two  Different Lists Using Lambda Function

'''
Function Name    :  Product Of Elements Of Two Different Lists . 
Function Date    :  9 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

lst1 = [1,2,3,4,5]
lst2 = [10,20,30,40,50]
lst3 = list(map(lambda x, y: x*y, lst1, lst2))
print(lst3)
