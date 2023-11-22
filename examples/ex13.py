"""
Example of recursive function.

For a given directory, display the `tree` view of files and subdirectories
"""
import os
from os import path


def print_tree(dir_name: str, indent='') -> None:
    print(f'{indent}{path.basename(dir_name)}')
    entries = os.listdir(dir_name)

    for entry in entries:
        entry_path = path.join(dir_name, entry)
        if path.isdir(entry_path):
            print_tree(entry_path, indent+'   ')
        else:
            print(f'{indent}  {entry}')


def main():
    dir_name = input('Enter directory: ')
    print_tree(dir_name)


if __name__ == '__main__':
    main()
