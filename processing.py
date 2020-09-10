# Python Program To Understand List Processing Methods

'''
Function Name    :  Processing Methods.
Function Date    :  10 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

num = [10,20,30,40,50]

n = len(num)
print('Number Of Elements In num : ', n)
print("\n Next")

num.append(60)
print('num After Appending 60 : ', num)
print("\n Next")

num.insert(0, 5)
print('num After Inserting 5 At oth Position : ', num)
print("\n Next")

num1 = num.copy()
print('Newly Created List num1 : ', num1)
print("\n Next")

num.extend(num1)
print('num After Appending num1 : ', num)
print("\n Next")

num.count(50)
print('Number Of Time 50 Found In The List num : ', n)
print("\n Next")

num.remove(50)
print('num After Removing 50 : ', num)
print("\n Next")

num.pop()
print('num After Removing Ending Elements : ', num)
print("\n Next")

num.sort()
print('num After Sorting : ', num)
print("\n Next")

num.reverse()
print('num After Reversing : ', num)
print("\n Next")

num.clear()
print('num After Removing All Elements : ', num)
print("\n Last")