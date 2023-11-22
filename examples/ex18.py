"""
More list comprehension example
"""


def to_code(txt: str, ch='#') -> str:
    return ''.join([ch if c in 'AEIOU' else c for c in txt.upper()])


def main():
    first_names = ['Anil', 'Shyam', 'Ajay', 'Anantha', 'John', 'Albert', 'Martin']
    codes = [to_code(fname, '$') for fname in first_names if fname.startswith('A')]
    print(codes)


if __name__ == '__main__':
    main()
