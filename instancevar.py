# Python Program To Understand Instance Variable

'''
Function Name    :  Understand Instance Variable.
Function Date    :  16 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Sample:
    # This Is A Constructor
    
    def __init__(self):
        self.x = 10
    
    # This Is An Instance Method
    
    def modify(self):
        self.x+=1
        
# Create 2 Instance

s1 = Sample()
s2 = Sample()
print('x in s1', s1.x)
print('x in s2', s2.x)

# Modify X In s1

s1.modify()
print('x in s1', s1.x)
print('x in s2', s2.x)


