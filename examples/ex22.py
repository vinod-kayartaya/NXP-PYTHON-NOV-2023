#! /usr/bin/python3
"""
An example for understanding exceptions.
"""
import sys


def main():
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]

        num = int(arg1)
        den = int(arg2)

        quot = num // den
        rem = num % den

        print(f'{num}/{den} will yield a quotient of {quot} with remainder of {rem}.')
    except ZeroDivisionError as err:
        print(f'Cannot divide an integer by zero\n[Error raised: {err}]')
    except IndexError as err:
        print(f'Expected 2 arguments, but received {len(sys.argv)-1}\n[Error raised: {err}]')
    except ValueError as err:
        print(f'Expected 2 integers\n[Error raised: {err}]')
        # return  # go back to the called location
        exit(1)  # go back to the OS, without returning to the caller; but `finally` is still executed
    finally:
        print('this gets executed in all scenarios')

    print('This is the last line in the main() method')


if __name__ == '__main__':
    main()
    print('End of script execution')
    # python ex22.py 1234 33
    # python ex22.py 1234 0
    # python ex22.py 1234 asdf
    # python ex22.py 1234
