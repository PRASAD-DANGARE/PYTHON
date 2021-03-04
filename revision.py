'''
Description      :  Accept Number & Display Summation Of All Numbers, Find Even, Perfect, Prime Numbers
Function Date    :  04 Mar 2021
Function Author  :  Prasad Dangare

'''

# Design Object Oriented Python Application Which Accepts N Number From User And Perform Below Operations

# Calculate The Summation Of All Numbers 
# Display All Even Numbers
# Display All Perfect Number 
# Display All Prime Numbers

class Numbers:
    
    def __init__(self,no = 10): # create init method(Constructor)
        self.size = no # instance variable(size)
        self.arr = []

    def __del__(self): # del Method
        print("Dealocating The Memory Of Objects")
        del self.arr

    def Accept(self): # Instance Method
        print("Please Enter The Elements")
        for i in range(self.size):
            print("Enter number : ", i+1)
            self.arr.append(int(input()))

    def Display(self): # Display Whole List Elements
        print("Elements of list is ")
        for i in range(self.size):
            print(self.arr[i])

    def Summation(self):
        sum = 0
        for i in range(self.size):
            sum = sum + self.arr[i]
        return sum
    
    def EvenDisplay(self):
        print("Even elements from list are : ")
        for i in range(self.size):
            if(self.arr[i]%2) == 0:
                print(self.arr[i])

    def PerfectDisplay(self):
        sum = 0
        for i in range(self.size):
            for j in range(1,int(self.arr[i]/2)+1): # O(N/2) With + 1 Is equal to Half Of The N Number.
                if(self.arr[i]%j) == 0:
                    sum = sum + j
            if sum == self.arr[i]:
                print(self.arr[i])
            sum = 0

    def PrimeDisplay(self):
        Flag = False
        for i in range(self.size):
            for j in range(2,int(self.arr[i]/2)+1):
                if(self.arr[i]%j) == 0:
                    Flag = True
                break

            if Flag == False:
                print(self.arr[i])
            Flag = False

def main():

    print("Enter Number Of Elements")

    value = int(input())
    obj1 = Numbers(value)

    obj1.Accept()

    obj1.Display()
    
    ret = obj1.Summation()
    print("Summation of all elements :", ret)
    
    obj1.EvenDisplay()
    
    print("Perfect numbers are : ")
    obj1.PerfectDisplay()
    
    print("Prime numbers are")
    obj1.PrimeDisplay()
    
    del obj1 # delete the object

if __name__ == "__main__":
    main()