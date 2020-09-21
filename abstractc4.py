# Python Program In Which RollsRoyce Sub Class Implements The Abstract Methods Of The Super Class, Car

'''
Function Name    :  Sub Class From abstractc2 class 
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from abstractc2 import Car
class RollsRoyce(Car):
    
    def steering(self):
        print('RollsRoyce')
        print('Drive The Car')
        
    def breaking(self):
        print('RollsRoyce Uses Authomatc Breaks')
        print('Apply Breaks And Stop It')
        
# Create Objects To RollsRoyce And Use Its Features

s = RollsRoyce(9030)
s.openTank()
s.steering()
s.breaking()

