'''Math :- Floor, Ceil, Sqrt, fmod, fsum, fabs and factorial'''
from math import*
#import math                                        # If imported like this, 'math' should be typed before every function. Fpr ex. math.floor()

print(floor(3.71))                  # [10]                # 'floor' will round the number down to the nearest whole number i.e. he number before the decimal.
print(floor(-3.8))                  # [11]

print(ceil(3.001))                  # [12]                # 'ciel' will round the number up to the next whole number if there are any numbers after the decimal.
print(ceil(-4.41))

print(sqrt(64))                     # [13]                # Finds the square root of the number.

print(fmod(13, 5))                  # [12]                # Prints out the remainder in float.

print(fsum((2, 3, 4, 5, 1)))        # [13]                # Will add all the numbers in the iterable/ sequence. like tuple, list, set.

print(fabs(-4))                     # [14]                # The positive value of that number in float.

print(factorial(6))                 # [15]                # Prints the factorial of the number. For ex. 5! = 5*4*3*2*1
