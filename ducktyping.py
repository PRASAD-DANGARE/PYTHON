# Python Program To Invoke A Method On An Object Without Knowing The Type Or Class Of The Object

'''
Function Name    :  Duck Typing Philosophy In Python
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

# Duck Class Contain talk() Method

class Duck:
    def talk(self):
        print('Quack , quack ! ')
        
# Human Class Contain talk() Method

class Human:
    def talk(self):
        print('Hello , Hi ! ')
        
# This Method Accepts An Object And call talk() Method

def call_talk(obj):
    obj.talk()
    
# Call Call_talk() Method And Pass An Object
# Depending On Type Of Object, talk() Method Is Executed

x = Duck()

call_talk(x)
x = Human()
call_talk(x)
 