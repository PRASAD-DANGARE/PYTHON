# Python Program To Understand The Order Of Execution Of Methods In Several Base Classes According To MRO

'''
Function Name    :  Multiple Inheritance With Several Classes In MRO
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class A(object):
    def method(self):
        print('A Class Methhod')
        super().method()
        
class B(object):
    def method(self):
        print('B Class Method')
        super().method()
        
class C(object):
    def method(self):
        print('C Class Method')
        
class X(A, B):
    def method(self):
        print('X Class Method')
        super().method()
        
class Y(B, C):
    def method(self):
        print('Y Class Method')
        super().method()
        
class P(X, Y, C):
    def method(self):
        print('P Class Method')
        super().method()
        
p = P()
p.method()
    