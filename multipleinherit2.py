# Python Program To Prove That Only One Class Constructor Is Available To Sub Class In Multiple Inheritance

'''
Function Name    :  Super Class Have Constructors
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)
        
class B(object):
    def __init__(self):
        self.b = 'b'
        print(self.b)
        
class C(A, B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()
        
# Access The Super Class Instance vars From c

o = C()
