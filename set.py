'''
Description      :  Demonstration Of Set 
Function Date    :  16 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Hetrogenious elements
Output           :  --
'''


print("Demonstration Of Set")

MarvellousSet = {11, "PPA", 21, 3.14, "Python"}

print(MarvellousSet) # {'Python', 3.14, 'PPA', 11, 21}
print(len(MarvellousSet)) # 5

MarvellousSet.remove(21)
print(MarvellousSet) # {3.14, 11, 'Python', 'PPA'}

MarvellousSet.discard(11) # use for removes the element, 
                          #If the element is not present in the set, then no error or exception is raised
print(MarvellousSet) # {'Python', 3.14, 11, 'PPA'}

MarvellousSet.add("Angular") # add is use to add the element in the set
print(MarvellousSet) # {3.14, 'Python', 'Angular', 'PPA'}