# Python Program To Show Variable Length Argument And Its Value

'''
Function Name    :  Show Variable Length Argument And Its Value. 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String  
'''

def add(farg, *args): # *args Can Take 0 Or More Values
    """ To Add Given Numbers """
    
    print('\n Formal Arguments = ', farg)
    
    sum = 0
    for i in args:
        sum += i
    print('Sum Of All Numbers = ', (farg + sum))
    print("\n")
# Call add() And Pass Arguments

add(5, 10)
add(5, 10, 20, 30)
