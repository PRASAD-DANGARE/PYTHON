# Python Program To Implement Multiple Inheritance Using Two Base Classes

'''
Function Name    :  Implement Multiple Inheritance Using Two Base Classes
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Father:
    def height(self):
        print('Height Is 5.7 Foot ')
        
class Mother:
    def color(self):
        print('color is brown ')
        
class child(Father, Mother):
    pass

c = child()
print('Child\' S inherited qualities : ')
c.height()
c.color()
