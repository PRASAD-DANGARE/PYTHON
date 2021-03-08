'''
Description      :  Public Can Access Outside Of A Class, 
                    Proctected Can Access Only For Derived Class, 
                    Private Is Accessable Only In That Particular Class.

Function Date    :  08 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

class Demo:
    def __init__(self): # init Method(Constructor)
        self.public = 10 # Attributes Public, Proctected, Private(Instance Variable)
        self._protected = 20 
        self.__private = 30
        
    def publicfun(self): # Public Method
        print("public fun")
        
    def _protectedfun(self): # Proctected Method
        print("protected fun")
     
    def __privatefun(self): # Private Method
        print("private fun")
        
obj = Demo() # Create object of Demo Class
print(obj.public)
print(obj._protected)
obj.publicfun()
obj._protectedfun()

#obj.__privatefun() not allowed
#print(obj.__private) not allowed
