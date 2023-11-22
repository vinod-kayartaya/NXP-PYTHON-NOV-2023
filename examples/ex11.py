"""
Given a directory path, display the list of all files and subdirectories in it.
"""
import os


def list_files_and_dirs():
    dir_name = input('Enter path to list files: ')
    if not os.path.exists(dir_name):
        print('Invalid path given')
        return

    files = os.listdir(dir_name)
    i = 1
    for file in files:
        full_path = os.path.join(dir_name, file)
        file_type = 'directory' if os.path.isdir(full_path) else 'file'
        print(f'{i}. {file} ({file_type})')
        i += 1


def main():
    list_files_and_dirs()


if __name__ == '__main__':
    main()
