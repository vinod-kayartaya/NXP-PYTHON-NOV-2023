"""
More complex conditional statements.

Accept a number for year and check if it is leap or not.
"""


def is_leap(year: int) -> bool:
    """
    Checks if the year supplied as argument is a leap year or not

    :param year: year to check
    :return: True if year is a leap; else False
    """
    if type(year) is not int:
        raise TypeError('Invalid type for year. Must be an int')

    if year < 1900:
        raise ValueError('Invalid value for year. Must be >= 1900')

    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def main():
    y = int(input('Enter a number for year: '))
    y = 'asdf'
    if is_leap(y):
        print(f'{y} is a leap year!')
    else:
        print(f'{y} is not a leap year.')


if __name__ == '__main__':
    main()
