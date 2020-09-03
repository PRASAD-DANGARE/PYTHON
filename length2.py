# Python Program To Find The Number Of Words In A String

'''
Function Name    :  Find LNumber Of Words In A String. 
Function Date    :  3 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String,Integer
'''

str = input('\n Enter A String : ')
print("\n")

i = c = 0
flag = True # This Becomes False When No Space Is Found
for s in str:

# Count Only When There Is No Space Previously

 if flag == False and str[i]==' ':
    c += 1

# If A Space Is Found Take flag As True

 if str[i]==' ':
    flag = True
 else:
     flag = False
     i += 1
print('Number Of Words : ', c + 1)
print("\n")