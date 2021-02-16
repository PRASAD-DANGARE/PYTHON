'''
Description      :  Demonstration Of Tuple 
Function Date    :  16 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Hetrogenious elements
Output           :  --
'''


print("Demonstration of Tuples")
tup = (11,"Marvellous",3.14,51,"Infosystems")

print(tup) # (11, 'Marvellous', 3.14, 51, 'Infosystems')
print(tup[0]) # 11
print(tup[1]) # Marvellous
print(tup[1:]) # ('Marvellous', 3.14, 51, 'Infosystems')
print(tup[:2]) # (11, 'Marvellous')
print(tup[1:2]) # ('Marvellous',)

# tup[1] = "marvellous" It is not allowed to change the contents

print(len(tup)) # 5
print("Marvellous" in tup)
del tup # True