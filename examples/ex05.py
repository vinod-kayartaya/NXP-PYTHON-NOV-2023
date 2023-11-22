"""
Example of using `if` statement
Let's accept a number from the user and check if it is an even or odd number
"""


def start():
    num = input('Enter an integer: ')

    if not num.isdigit():
        print('Only integer was expected!')
        return

    num = int(num)
    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')


if __name__ == '__main__':
    start()
    print('End of script')
