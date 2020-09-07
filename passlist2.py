# Python Program To Pass A List To A Function And Modify It

'''
Function Name    :  Pass A List To A Function And Modify It. 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer 
'''

def modify(lst):
    """ To Add A New Elements To List """
    
    lst.append(9)
    print(lst, id(lst))
    
# Call Modify() Function And Pass lst

lst = [1,2,3,4]
modify(lst)
print(lst, id(lst))
