'''
Description      :  Dynamic Input 
Function Date    :  22 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

print("Demonstration of Dynamic Input In List")

arr = list() # Create Object of List

num = input("Enter How Many Elements You Want : ")
print ("Enter Numbers In List : ") # Ask the user about the number of elements

for i in range(0,int(num)): # Iterate the for loop to accept N numbers

    no = input("Enter Number : ") # Accept individual element from user
    arr.append(int(no)) # Insert that element into List
    print ("Entered Elements Are : ",arr)