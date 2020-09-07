# Python Program To Understand Keyword Variables Arguments

'''
Function Name    :  Use Of Keyword Variable Arguments. 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String  
'''

def display(farg, **kwargs): # **kwarg Can Take 0 Or More Values
    """ to display given values """
    
    print('Formal Arguments = ', farg)
    
    for x, y in kwargs.items(): # items() Will Give Pairs Of Items
        print('key = {}, value = {}'.format(x, y)) 
        
# Pass 1 Formal Arguments And 2 Keyword Arguments

display(5, rno = 10)
print()

# Pass 1 Formal Argument And 2 Keyword Arguments 

display(5, rno = 10, name = 'Prasad')
