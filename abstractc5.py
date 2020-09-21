# Python Program To Develop An Interface That Connects To Any DataBases

'''
Function Name    :  Develop An Interface That Connects To Any DataBases
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from abstractc2 import*
class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
# This Is A Sub Class

class Oracle(Myclass):
    def connect(self):
        print('Connecting To Oracle DataBase...')
        
    def disconnect(self):
        print('Disconnect From Oracle..')
        
# This Is Another Sub Class

class Sybase(Myclass):
    def connect(self):
        print('Connecting To SyBase DataBase...')
        
    def disconnect(self):
        print('Disconnect From SyBase') 
        
class DataBase:
    
    # Accept DataBase Name As String
    
    str = input('Enter DataBase Name : ')
    
    # Convert The String Into Classname
    
    classname = globals()[str] 
    
    # Create An Object To That Classname
    
    x = classname()
    
    # call The Connect() And Disconnect() Method
    
    x.connect()
    x.disconnect()
    
          