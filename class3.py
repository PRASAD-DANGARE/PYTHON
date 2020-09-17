# Python Program To Create A Static Method That Counts The Number Of Instances Created For A Class

class Myclass:
    
    # This Is Class Variable Or Static Variable
    
    n = 0
    
    # Constructor That Increments n When An Instance Is Created
    
    def __init__(self):
        Myclass.n = Myclass.n+1
        
    # This Is A Static Method To Display The no. Of Instances
    @staticmethod
    def noObjects():
        print('No Of Instances Created : ', Myclass.n)
        
# Create 3 Instances

obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
Myclass.noObjects()
