# Python Program To Undeerstand Class Variables Or Static Variable


'''
Function Name    :  Understand Class Or Static Variable.
Function Date    :  16 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''


class Sample:
    # This Is A Class Var
    x = 10
    
    # This Is  Class Method
    
    @classmethod
    def modify(cls):
        cls.x+=1
        
# Create 2 Instances

s1 = Sample()
s2 = Sample()
print('x in s1 = ', s1.x)
print('x in s2 = ', s2.x)

# Modify x In s1

s1.modify()
print('x in s1 = ', s1.x)
print('x in s2 = ', s2.x)

