# Python Program Which Contains A Printer Interface And Its Sub Classes To Send Text To Any Printer

'''
Function Name    :  An Interface Send Text To Any Printer
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from abstractc2 import*

# Create An Interface

class printer(ABC):
    @abstractmethod
    def printit(self, text):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
# This Is Sub Class For IBM Printer

class IBM(printer):
    def printit(self, text):
        print(text)
        
    def disconnect(self):
        print('printing completed on IBM printer..')

# This Is Sub Class For Epson Printer

class Epson(printer):
    def printit(self, text):
        print(text)

    def disconnect(self):
        print('printing completed on Epson printer')
        
# Class Useprinter

# Accept Printer Name As A String From Configuration File 

with open("abstractc7.txt", "r") as f:
    str = f.readline()
    
# Convert The String Into Classname

classname = globals()[str]

# Create An Object To That Class

x = classname()

# Call The printit() And Disconnect() Methods

x.printit('Hello, this is sent to printer')
x.disconnect()
