# Python Program To Create Teacher Class And Store It Into teacher.py

'''
Function Name    :  Creating Teacher Class 
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from os import name


class Teacher:
    def setid(self, id):
        self.id = id
        
    def getid(self):
        return self.id
    
    def setname(self, name):
        self.name = name
        
    def getname(self):
        return self.name
    
    def setaddress(self, address):
        self.address = address
        
    def getaddress(self):
        return self.address
    
    def setsalary(self, salary):
        self.salary = salary
        
    def getsalary(self):
        return self.salary
    
    