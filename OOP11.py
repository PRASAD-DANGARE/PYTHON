'''
Description      :  Demonstration Of Public, Private, Proctected (Like Access Specifier) 
Function Date    :  08 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

# Access specifier Public & Non Public (Private, Proctected) there is no concept like Access specifier but we can relate it

# public : no1
# proctected : _no2
# private : __no3

class Base:

    def __init__(self):
        self.no1 = 11           # public member
        self._no2 = 21          # protected member
        self.__no3 = 51         # private member

    def fun(self):                  # public method
        print(self.no1, self._no2, self.__no3)
        
    def _fun(self):                  # protected method
        print(self.no1, self._no2, self.__no3)
            
    def __fun(self):                  # private method
        print(self.no1, self._no2, self.__no3)
                    
class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        
    def gun(self):
        print(self.no1)
        print(self._no2)
        #print(self.__no3)          Not allowed
        self.fun()  # method call of base class
        self._fun()
        # self.__fun()                  Not allowed

def main():

    bobj = Base()  # create object of Base class
    print(bobj.no1)
    print(bobj._no2)
    #print(bobj.__no3)      Not allowed
    
    bobj.fun()
    bobj._fun()
    # bobj.__fun()              Not allowed
    
    dobj = Derived() # create object of Derived class
    dobj.gun()
    print("Dobj.gun")
    
if __name__ == "__main__":
    main()
