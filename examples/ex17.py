"""
An example to understand `list comprehension` technique
"""
import math


def main():
    nums = [12, 23, 34, 45, 11, 29, 49, 22, 49, 10]
    even_nums = [num for num in nums if num % 2 == 0]
    odd_nums = [n for n in nums if n % 2]  # 0 --> False, non-zero --> True
    last_digits = [n % 10 for n in nums]
    squares = [n * n for n in nums]
    even_squares = [n * n for n in nums if n % 2 == 0]
    sqrts = [round(math.sqrt(n), 2) for n in nums]

    print(f'even_nums is {even_nums}')
    print(f'odd_nums is {odd_nums}')
    print(f'last_digits is {last_digits}')
    print(f'squares is {squares}')
    print(f'even_squares is {even_squares}')
    print(f'sqrts is {sqrts}')


if __name__ == '__main__':
    main()
