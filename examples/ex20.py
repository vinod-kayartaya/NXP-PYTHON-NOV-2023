import sys


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def to_float(s):
    try:
        return float(s)
    except ValueError:
        return None


def main():
    # args = [float(arg) for arg in sys.argv if is_float(arg)]
    args = [to_float(arg) for arg in sys.argv]
    args = [arg for arg in args if arg is not None]

    print(f'count = {len(args)}')
    print(f'sum = {sum(args)}')
    print(f'average = {sum(args) / len(args)}')


def print_args_info():
    print(f'This script was executed with {len(sys.argv)} command line arguments')
    print(f'The command line arguments are:')
    for arg in sys.argv:
        print(f'\t{arg}')


if __name__ == '__main__':
    main()
