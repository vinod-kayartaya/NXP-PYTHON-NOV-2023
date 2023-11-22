"""
Dealing with number inputs
"""
import math


num = input('Enter a number, I will give the square and square-root of the same: ')
# print(f'type of num is {type(num)}')
num = float(num)
# print(f'type of num is {type(num)}')
square = num ** 2  # num * num
square_root = math.sqrt(num)

print(f'square of {num} is {square} and square root of the same is {square_root}')
