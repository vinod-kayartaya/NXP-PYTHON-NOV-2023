"""
A small menu-driven application to work with SQLite database
"""


if __name__ == '__main__':
    while True:
        print("""Main Menu:
        1. Create CUSTOMERS table
        2. Add a new customer record
        3. List all customers
        4. Search customer by id
        5. Edit customer data
        6. Exit
        """)
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                print('Choice not implemented yet\n\n')
            elif choice == 2:
                print('Choice not implemented yet\n\n')
            elif choice == 3:
                print('Choice not implemented yet\n\n')
            elif choice == 4:
                print('Choice not implemented yet\n\n')
            elif choice == 5:
                print('Choice not implemented yet\n\n')
            elif choice == 6:
                print('Thank you, have a nice day!')
                break
            else:
                print('Invalid choice. Please try again')
        except ValueError:
            print('Invalid choice. Please try again')