'''
Description      :  Demonstration Of Function Arguments 
Function Date    :  14 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

print("\nDemonstration of Types of Function Arguments")

# Position arguments (required according to there value and order )

def Batches1(name,fees):
    print("Batch name is ", name)
    print("Fees are ", fees)
    
print("\nDemonstration of Position Arguments")
    
# Keyword Arguments (mendotery but sequence is not order wise)

Batches1('Python', 5000) # value of Batches1 as per the sequence
Batches1(5000,'Angular') # value of Batches2 not as per the order

def Batches2(name,fees):

    print("Batch name is ", name)
    print("Fees are ", fees)
    
print("\nDemonstration Keyword of Arguments")
    
Batches2(fees=9000, name='PPA')
Batches2(name='LB',fees=7500)

# Default Arguments (if no input is given then it take default value)

def Batches3(name,fees = 5000):

    print("Batch name is ", name)
    print("Fees are ", fees)
    
print("\nDemonstration of Default Arguments")
    
Batches3('Angular',7500)
Batches3('Angular')
Batches3(fees=9000, name='PPA')
Batches3(name='LB')

# Variable number of arguments (if input is not known or infinite)

def Add(*no):

    ans = 0
    for i in no:
        ans = ans + i
    return ans
    
print("\nDemonstration of Variable number of Arguments")
ret = Add(10,20,30)

print("Addition is ",ret)
ret = Add(10,20,30,40,50,60)

print("Addition is ",ret)
ret = Add(10,20)

print("Addition is ",ret)

# Keyword Variable number of arguments

def StudentInfo(**other):

    print(other)
    for i,j in other.items():
        print(i,j)
    
print("\nDemonstration of Keyword Variable number of Arguments")

StudentInfo(age = 28, address = "Sinhagad Road", mobile = 7588945488, company = "Marvellous")
