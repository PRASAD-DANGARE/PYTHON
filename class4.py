# Python Program To Create A Static Method That Calculates The Square Root Value Of A Given Number

'''
Function Name    :  Static Method To Find Square Root Value.
Function Date    :  17 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

import math
class Sample:
    @staticmethod
    def calculate(x):
        result = math.sqrt(x)
        return result
    
# Accept A Number From Keyboard

num = float(input('Enter A Number : '))

# Call The Static Method And Pass num

res = Sample.calculate(num)
print('The Square Root Of {} Is {:.2f}'.format(num, res))
