'''
Description      :  Use Of getsizeof In Sys
Function Date    :  14 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

import sys

no = 11

print(no) # 11
print(id(no)) # 140719579072480

print(type(no)) # <class 'int'>
print(sys.getsizeof(no)) # 28
print("\n")

f = 11.45

print(f) # 11.45
print(id(f)) # 2022333974384

print(type(f)) # class 'float'>
print(sys.getsizeof(f)) # 24
print("\n")

str = "HelloA"

print(str) # HelloA
print(id(str)) # 2134709239216

print(type(str)) # <class 'str'>
print(sys.getsizeof(str)) # 55