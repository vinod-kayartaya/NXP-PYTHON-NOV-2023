"""
This is an example `for` loop with `range` object
"""


def print_primes_between(start: int, end: int) -> None:
    for n in range(start, end+1):
        if is_prime(n):
            print(n, end=', ')
    print()


def is_prime(num: int) -> bool:
    if num < 2:
        return False

    start = 2
    stop = num // 2 + 1
    for d in range(start, stop):
        if num % d == 0:
            return False

    return True


def main() -> None:
    n = int(input('Enter FROM: '))
    m = int(input('Enter TO: '))
    print_primes_between(n, m)


if __name__ == '__main__':
    main()
