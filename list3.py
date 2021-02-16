'''
Description      :  Demonstration Of List 
Function Date    :  16 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Hetrogenious elements
Output           :  --
'''

print("Demonstration of List")
batches = ["PPA","LB","Angular","Python"]

print(batches) # ['PPA', 'LB', 'Angular', 'Python']
print(batches[0]) # PPA
print(batches[1]) # LB
print(batches[-1]) # Python
print(batches[1:]) # ['LB', 'Angular', 'Python']
print(batches[:3]) # ['PPA', 'LB', 'Angular']

# we can store heterogenious data
data1 = [11,"Marvellous",3.14]
print(data1) # [11, 'Marvellous', 3.14]

data2 = [21,"Infosystems",6.10]
print(data2) # [21, 'Infosystems', 6.1]

# We can create list of list
combined = [data1, data2]
print(combined) # [[11, 'Marvellous', 3.14], [21, 'Infosystems', 6.1]]

# There are multiple methods that we can use to manipulate list
batches.append("MEAN")
print(batches) # ['PPA', 'LB', 'Angular', 'Python', 'MEAN']

batches.insert(2,"LSP")
print(batches) # ['PPA', 'LB', 'LSP', 'Angular', 'Python', 'MEAN']

batches.remove("LSP")
print(batches) # ['PPA', 'LB', 'Angular', 'Python', 'MEAN']

batches.pop()
print(batches) # ['PPA', 'LB', 'Angular', 'Python']

batches.pop(2)
print(batches) # ['PPA', 'LB', 'Python']

del batches[1:]
print(batches) # ['PPA']

batches.extend(["LB","Python","Angular","MEAN"])
print(batches) # ['PPA', 'LB', 'Python', 'Angular', 'MEAN']

batches.sort()
print(batches) # ['Angular', 'LB', 'MEAN', 'PPA', 'Python']