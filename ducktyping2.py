# Python Program To Call A Method That Does Not Appear In The Object Passed To The Method

'''
Function Name    :  Call A Method That Does Not Appear In The Object
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

# Dog Class Contain bark() Method

class Dog:
    def bark(self):
        print('Bow , Wow ! ')
        
# Duck Class Contain talk() Method

class Duck:
    def talk(self):
        print('Quack, quack ! ')
        
# Human Class Contain talk() Method

class Human:
    def talk(self):
        print('Hello , Hi  ! ')
        
# This Method Accepts An Object And Calls talk() Method

def call_talk(obj):
    obj.talk()
    
# call call_talk() Method And Pass An Object
# Depending On Type Of Object , talk() Method Is Executed

x = Duck()
call_talk(x)
x = Human()
call_talk(x)
x = Dog()
call_talk(x) # Error
