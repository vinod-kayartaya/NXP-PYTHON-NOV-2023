"""
Example of using a loop

1. `while` loop
2. `for` loop
"""


def print_table():
    num = int(input('Enter a number: '))
    i = 1
    while i <= 10:
        print(f'{num} X {i} = {num*i}')
        i += 1


def menu() -> int:
    print("""Main Menu:
    1. Add new customer data
    2. Search and edit customer data
    3. Search and delete customer data
    4. Exit""")
    return int(input('Enter your choice: '))


def main():
    while True:
        choice = menu()
        if choice == 1:
            print('Add new customer module not ready yet!')
        elif choice == 2:
            print('Edit customer module not ready yet!')
        elif choice == 3:
            print('Delete customer module not ready yet!')
        elif choice == 4:
            break
        else:
            print('Invalid choice. Please try again')

    print('Thank you and have a nice day')


if __name__ == '__main__':
    # main()
    print_table()