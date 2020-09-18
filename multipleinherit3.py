# Python Program To Access All The Instance Variable Of Both The Base Classes In Multiple Inheritance 

'''
Function Name    :  Access Instance Variable Of Both The Base Class In Multiple Inheritance
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)
        super().__init__()
        
class B(object):
    def __init__(self):
        self.b = 'b'
        print(self.b)
        super().__init__()
        
class C(A, B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()
        
# Access The Super Class Instance vars From c

o = C()
