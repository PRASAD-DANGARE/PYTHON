# Python Program To Create A New Object Inside The Function Does Not Modify Outside Object

'''
Function Name    :  Create New Object Inside Function Does Not Modify Outside Object. 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer 
'''

def modify(lst):
    """ To Create A New List """
    
    lst = [10,11,12]
    print(lst, id(lst))
    
# Call Modify And Pass lst

lst = [1,2,3,4]
modify(lst)
print(lst, id(lst))
