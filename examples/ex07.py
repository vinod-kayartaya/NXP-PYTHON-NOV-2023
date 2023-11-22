"""
More example of using if-elif-else constructs

Find the maximum number of days in a given month/year combination
"""
from ex06 import is_leap


def max_days(month: int, year: int) -> int:
    if type(month) is not int or type(year) is not int:
        raise TypeError('month and year must be int')

    if year < 1900:
        raise ValueError('year must be >= 1900')

    if month < 1 or month > 12:
        raise ValueError('month must be between 1 and 12')

    if month == 2:
        md = 29 if is_leap(year) else 28  # md = is_leap(year) ? 29: 28
    elif month in (4, 6, 9, 11):
        md = 30
    else:
        md = 31

    return md


def main():
    m = int(input('Enter month: '))
    y = int(input('Enter year: '))
    days = max_days(m, y)
    print(f'the {m} month of {y} year has {days} days')


if __name__ == '__main__':
    main()
