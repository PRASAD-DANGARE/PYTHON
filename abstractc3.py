# Python Program In Which Mercedes Is Sub Class Implements The Abstract Method Of Super Class, Car

'''
Function Name    :  We Use abstractc2 class in this program
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from abstractc2 import Car
class Mercedes(Car):
    def steering(self):
        print('Mercedes Uses Manual And Automatic Steering')
        print('Drive the car')
    
    def breaking(self):
        print('Mercedes Uses Brake Assist System BAS')
        print('Apply Breaks And Stop It')
        
# Create Objects To Mercedes And Use Its Features

m = Mercedes(63)
m.openTank()
m.steering()
m.breaking()



