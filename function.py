'''
Description      :  Performing New Variations In Functions  
Function Date    :  08 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Str
Output           :  Str
'''

print("Demonstration Of Advanced Functions ")

# 1 : Function Which Accepts Nothing And Return Nothing

def Marvellous1():
    print("Inside Marvellous1")
    

# 2 : Function Which Accepts Parameters And Returns Nothing

def Marvellous2(no):
    print("Inside Marvellous2 ")
    print("Accepted Value Is :", no)

    
# 3 : Function Which Accepts Parameter And Return The Value

def Marvellous3(no):
    print("Inside Marvellous3 ")
    print("Accepted Value Is :", no)
    return no + 1

    
# 4 : Function Which Accepts Multiple Values And Return Multiple Values

def Marvellous4(value1, value2):
    print("Inside Marvellous4 ")
    add = value1 + value2
    sub = value1 - value2
    return add, sub


# 5 : Function Which Calls Another Function Which Is Defined Outside It

def Marvellous5():
    print("Inside Marvellous5 ")
    Marvellous1()


# 6 : Function Which Contain Another Nested Function Defined In It

def Marvellous6():
    print("Inside Marvellous6")
    
    def InnerFun():
        print("Inside Inner Fun")
    InnerFun()
    
    
def main():
    no = 11
    
    Marvellous1()
    
    Marvellous2(no)

    ret = Marvellous3(no)
    print("Return Value Is : ",ret)

    ret1, ret2 = Marvellous4(10, 4)
    print("Addition is : ",ret1)
    print("Substrin is : ",ret2)

    Marvellous5()

    Marvellous6()
    
if __name__ == "__main__":
    main()
