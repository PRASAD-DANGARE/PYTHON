# Python Program To Convert A String Into Key-Value Pairs And Store Them Into A Dictionary

'''
Function Name    :  Convert String Into Key-Value Pairs And Store It.
Function Date    :  13 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

str ="Prasad = 23, Shubham = 20, Hritik = 19, Shiva = 22"

# Brake The String At ',' And Then At '='
# Store The Pieces Into A List lst

lst = []
for x in str.split(','):
    y = x.split('=')
    lst.append(y)
    
# Convert The List Into Dictionary 'd'
# But This 'd' Will Have Both Name As String

d = dict(lst)

# Create A New Dictionary 'd1' With Name As String
# And Age As Integer

d1 = {}
for k, v in d.items():
    d1[k] = int(v)
    
# Display The Final Dictionary

print(d1)
 