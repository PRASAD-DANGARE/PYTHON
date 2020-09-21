# Python Program To Create A Car Abstract Class That Conatins An Instance Variable, 
# A Concrete Method And Two Abstract mMethods

'''
Function Name    :  Abstract Class With Instance Variable
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from abc import*
class Car(ABC):
    def __init__(self, regno):
        self.regno = regno
        
    def openTank(self):
        print('Fill The Fuel Into The Tank')
        print('For The Car With Rengo', self.regno)
        
    @abstractmethod
    def steering(self):
        pass
    
    @abstractmethod
    def breaking(self):
        pass
    