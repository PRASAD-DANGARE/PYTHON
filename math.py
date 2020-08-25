# import math library with all mathematical functions
import math

# 1 round a number upward to its nearest integer using math.ceil

print (math.ceil(1.4))
print (math.ceil(22.6))
print("Next1\n")

# 2 round a number downwards to its nearest integer using math.floor

print (math.floor(1.4))
print (math.floor(22.6))
print("Next2\n")

# 3 convert angles from radians to degrees using math.degrees

print (math.degrees(8.90))
print (math.degrees(90))
print("Next3\n")

# 4 convert different degrees into radians using math.radians

print (math.radians(180))
print (math.radians(-20))
print("Next4\n")

# 5 returns sine of different values using math.sin

print (math.sin(0.00))
print (math.sin(math.pi/2))
print(math.sin(-1.23))
print("Next5\n")

# 6 returns cosine of different values using math.cos

print (math.cos(0.00))
print (math.cos(-1.23))
print (math.cos(3.14159265359))
print("Next6\n")

# 7 returns tangent of different numbers using math.tan

print (math.tan(90))
print (math.tan(-90))
print("Next7\n")

# 8 find exponential of specified value using math.exp

print (math.exp(65))
print(math.exp(-6.89))
print("Next8\n")

# 9 remove sign of given numbers using math.fabs

print (math.fabs(-66.43))
print (math.fabs(-7))
print("Next9\n")

# 10 returns factorial of numbers using math.factorial

print (math.factorial(9))
print (math.factorial(12))
print("Next10\n")

# 11 sum of all items in tuple using math.fsum

a = (1,2,3,4,5)
print (math.fsum(a))
print("Next11\n")

# 12 returns remainder after module operatorusing math.fmod

print (math.fmod(67,7))
print (math.fmod(16,4))
print("Next12\n")

# 13 returns the base-10 logarithm of different numbers using math.log10

print (math.log10(2.7183))
print (math.log10(1))
print("Next13\n")

# 14 returns the natural logarithm of different numbers using math.log

print (math.log(2.7183))
print (math.log(1))
print("Next14\n")

# 15 returns the value of 9 raised to the power of 3 using math.pow

print (math.pow(9,3))
print("Next15\n")

# 16 find the highest number that can divide two numbers using math.gcd

print (math.gcd(26,12))
print (math.gcd(0,34))
print("Next16\n")

# 17 returns the square root of different numbers using math.sqrt

print (math.sqrt(25))
print (math.sqrt(16))
print("Next17\n")

# 18 returns truncated integer part of diffferent numbers using math.trunc

print (math.trunc(2.77))
print (math.trunc(-99.29))
print("Next18\n")

# 19 check whether some values are infinite using math.isinf

print (math.isinf(56))
print (math.isinf(+45.34))
print (math.isinf(math.inf))
print (math.isinf(float("nan"))) 
print (math.isinf(-math.inf))
print("Next19\n")

# 20 check whether same value are nan or not using math.isnan

print (math.isnan(56))
print (math.isnan(-45.34))
print (math.isnan(math.inf))
print (math.isnan(float("nan"))) 
print (math.isnan(float("-inf")))
print (math.isnan(math.nan))
print("Last20\n")
