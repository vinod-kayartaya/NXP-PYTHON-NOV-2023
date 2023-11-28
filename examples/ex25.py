"""
Example of a function with variable-length arguments
"""
import sys


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def find_average(n1, n2, *nums):
    print(f'nums is {nums}')
    print(f'type of nums is {type(nums)}')
    nums = [float(n) for n in (n1, n2, *nums) if is_float(n)]
    print(f'nums is {nums}')
    print(f'type of nums is {type(nums)}')
    return sum(nums) / len(nums)


def main():
    # a = find_average(10, 20, 30, 'vinod', 2.3, 44)
    # print(f'average is {a}')
    # a = find_average(20, 33)
    # print(f'average is {a}')
    a = find_average(*sys.argv)
    print(f'average is {a}')


if __name__ == '__main__':
    main()
