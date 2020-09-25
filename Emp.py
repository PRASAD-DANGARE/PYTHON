# Python Program To Create An Emp Class With Employee Details As Instance Variable

'''
Function Name    :  Create Emp Class With Employee Detail As Instance Variable
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        
    def display(self):
        print("{:5d} {:20s} {:10.2f}".format(self.id, self.name, self.sal))
        