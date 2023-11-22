"""
Example of a `for` loop.

Accept a bunch of numbers (user may input non-numerical values), and print
the sum of all int values
"""


def main():
    nums_str = input('Enter few numbers separated by a space: ')
    nums_list = nums_str.split(' ')
    total = 0
    for s1 in nums_list:
        if s1.isdigit():
            print(f'adding {s1}')
            total += int(s1)
        else:
            print(f'skipping "{s1}"')

    print(f'total of int inputs is {total}')


if __name__ == '__main__':
    main()
