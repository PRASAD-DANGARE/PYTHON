# Python Program To Sort The Elements Of A Dictionary Based On A Key Or Value

'''
Function Name    :  Sort Elements Of Dictionary Based On Key, Value.
Function Date    :  13 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

colors = {10: "Red", 35: "Green", 15: "Blue", 25: "White"}

# Sort The Dictionary By Keys i.e. 0th Elements

c1 = sorted(colors.items(), key = lambda t: t[0])
print(c1)

# Sort The Dictionary By Values , i.e. 1st Elements

c2 = sorted(colors.items(), key = lambda t: t[1])
print(c2)
