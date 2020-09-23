# Python Program To Create Our Own Exception And Raise It When Needed 

'''
Function Name    :  Create Our Own Exception And Raise It When Needed 
Function Date    :  23 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class allException(Exception):
    def __init__(self, arg):
        self.msg = arg
        
    # Write Code Where Exception May Raise
    # To Raise The Exception, Use Raise Statement
 
    def check(dict):
        for k,v in dict.items():
            print('Name= {:15s} Balance= {:10.2f}'.format(k,v))
            if(v<2000.00):
                raise allException('Balance Amount Is Less In The Account Of'+k)
            
    # Our Own Exception Is Handled Using try And except Blocks
    
    bank = {'Prasad' :5000.00, 'Hrutik' :8900.50, 'Shiva' :1990.00, 'Shubham' :3000.00}
    try:
      check(bank)
    except allException as me:
        print(me)