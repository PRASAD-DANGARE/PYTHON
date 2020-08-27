# Python Program To Calculate Area Of Circle

'''
Function Name    :  Area Of Circle
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Float
Output           :  Float
'''

import math


r = float(input('Enter  Radius:'))
area = math.pi *r**2 # pi Is A Constant In Math Module

print('Area Of Circle =',area)
print('Area Of Circle = {:0.2f}'.format(area))
