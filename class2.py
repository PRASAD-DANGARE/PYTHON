# Python Programs To Use Class Method To Handle The Common Features Of All The Instance Of Bird Class

'''
Function Name    :  Understanding Class Method.
Function Date    :  17 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

class Bird:
    # This Is A Class Variable
    
    wings = 2
    
    # This Is A Class Method
    
    @classmethod
    def fly(cls,name):
        print('{} Files With {} Wings'.format(name, cls.wings))
        
# Display Information For 2 Birds

Bird.fly('Sparrow')
Bird.fly('Pigeon')

