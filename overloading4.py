# Python Program To Show Method Overloading To Find Sum Of Two Or Three Numbers

'''
Function Name    :  Method Overloading To Find Sum Of Two Or Three Numbers
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print('Sum Of Three = ', a+b+c)
        elif a!=None and b!=None:
            print('Sum Of Two = ', a+b)
        else:
            print('Please Enter Two Or Three Arguments')
            
# call sum() Using Object

m = Myclass()
m.sum(10, 15, 20)
m.sum(10.5, 25.55)
m.sum(100)

