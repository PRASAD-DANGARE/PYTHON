'''
Description      :  types of function definations
Function Date    :  14 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

# types of function definations

# accepts nothing return nothing

def fun():
    print("inside fun")

# accepts parameters and return nothing

def gun(value):
    print("inside gun", value)

# accepts parameters and return the value

def sun(value):
    value = value + 1 
    print("inside sun")
    return value

# empty function

def mun():
    pass # it give space for now 

# nested function

def outer():
    print("inside outer")
    def Inner():
        print("inside inner")
    Inner()

def main():
    fun()
    gun(11)
    ret = sun(11)
    print(ret)
    mun()
    outer()

if __name__ == "__main__":
    main()