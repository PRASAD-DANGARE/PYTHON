# Python Program Using Command Line Arguments args
'''
Function Name    :  Command Line Arguments
Function Date    :  26 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer,String
Output           :  Integer,String
'''

import sys


n = len(sys.argv) # Use To Convert The Command Line , n Is The Number Of Arguments.

args = sys.argv # Use To Get All Variables Arguments List In args And Count It. Using sys.argv List Contain Arguments. 

print('No Of Command Line args=', n) # Is Use To Display All The Command We Pass In Runtime.

print('The args Are:', args) # Use To Pass A Variable Number Of Arguments.
print("\n")

print('The args One By One:') 
for a in args: print(a) # Use For-Loop To Display All The Command Line Arguments One By One.

'''
        (if i dont write prasad dangare in <"'> so it take it as 5 args prasad and dangare as different args)
       
         OUTPUT : args.py 93 "'Prasad Dangare'" 7057113124 
         No Of Command Line args= 4
         The args are: ['args.py', '93', "'Prasad Dangare'", '7057113124']
         
         The args One By One:
         args.py
         93
         'Prasad Dangare' 
         7057113124
'''