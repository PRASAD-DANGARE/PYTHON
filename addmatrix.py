# Python Program To Add Two Matrices And Display The Sum Matrix Using Lists

'''
Function Name    :  Add 2 Matrix And Display The Sum .
Function Date    :  11 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

# Take Matrix One With 3 Rows And 4 Columns
m1 = [ [1, 2, 3, 0],
       [4, 5, 6, 0],
       [7, 8, 9, 0] ]

# Take Matrix Two With 3 Rows And 4 Cols
m2 = [ [1, 2, 3, 4],
       [1, 0, 1, 0],
       [2, -1, -2, 1] ]

# Take Matrix Three With 3 Rows And 4 Cols And Initilize With All 0s
m3  = [4*[0] for i in range (3) ]

# Add The Corresponding Elements Of m1 And m2 And Store Into m3
for i in range(3):
    for j in range(4):
        m3[i][j] = m1[i][j] + m2[i][j]
        
# Display The Third Matrix Using For Loop
for i in range(3):
    
    for j in range(4):
        print('%d' %m3 [i][j], end='')
    print()
    