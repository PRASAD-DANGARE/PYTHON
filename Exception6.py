'''
Class Name       :  AgeInvalid()
Description      :  Exception Handling using try, except, else block
Function Date    :  21 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

class AgeInvalid(Exception):
    def __init__(self, data):
        self.data = data

def main():

    try:

        age = int(input("Enter Your Age for PAN card : "))
        if  age < 18:
            raise AgeInvalid("Your age is less than 18")

    except AgeInvalid as obj:
        print(obj)

    else:
        print("You will get the PAN card within 7 Working days")

if __name__ == "__main__":
    main()