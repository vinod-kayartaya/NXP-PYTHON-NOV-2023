"""
Example of a recursive function


f(n) = n * f(n-1)
     = n * (n-1) * f(n-2)

"""


def factorial(num: int) -> int:
    if num < 2:
        return 1
    return num * factorial(num-1)


if __name__ == '__main__':
    n = int(input('Enter a number: '))
    f = factorial(n)
    print(f'factorial of {n} is {f}')

