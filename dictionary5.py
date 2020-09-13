# Python Program To Convert The Elements Of Two Lists Into Key-Value Pairs Of A Dictionary

'''
Function Name    :  Convert Elements Of 2 Lists Into Key-Value Pairs.
Function Date    :  13 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

countries = ["USA", "India", "Germany", "France"]
cities = ['Washington', 'NewDelhi', 'Berlin', 'Pairs']

# Make A Dictionary 

z = zip(countries, cities)
d = dict(z)

# Display Key - Values Pairs From Dictionary d

print('{:15s} -- {:15s} '.format('COUNTRY', 'CAPITAL'))
for k in d:
    print('{:15s} -- {:15s} '.format(k, d[k]))
    
          