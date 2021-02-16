'''
Description      :  Demonstration Of Break & Continue In Loop 
Function Date    :  16 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

print("Demonstration of break & continue")
print("\nDemonstration of break")

for i in range(0,9):
    if(i == 4):
        break
    print(i)
print("\nDemonstration of continue")

for i in range(0,9):
    if(i == 3):
        continue
    print(i)