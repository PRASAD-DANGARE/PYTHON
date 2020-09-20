# Python Program To Check The Object Type To Know Whether The Method Exists In The Object Or Not

'''
Function Name    :  Check Object Type That The Method Exists In Object Or Not
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Dog:
    def bark(self):
        print('Bow, Wow ! ')
        
# Duck Class Contain talk() Method

class Duck:
    def talk(self):
        print('Quack , quack ! ')
        
# Human Class Contain talk() Method

class Human:
    def talk(self):
        print('Hello , Hi ! ')
        
# This Method Accepts An Object And Calls talk() Method

def call_talk(obj):
    if hasattr(obj, 'talk'):
        obj.talk()
    elif hasattr(obj, 'bark'):
        obj.bark()
    else:
        print('wrong object passed....')
        
# Call call_talk() Method And Pass An Object
# Depending On Type Of Object, talk() Method Is Executed

x = Duck()
call_talk(x)
x = Human()
call_talk(x)
x = Dog()
call_talk(x)

