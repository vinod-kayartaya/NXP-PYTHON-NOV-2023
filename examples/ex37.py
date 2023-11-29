#! /usr/bin/python3

"""
A small menu-driven application to work with SQLite database
"""
from sqlite3 import connect, DatabaseError

__DB_FILENAME = 'customers_db.sqlite'


def create_customers_table():
    sql_cmd = """create table customers(
    id integer primary key autoincrement,
    name varchar(50) not null,
    email varchar(255) unique,
    phone varchar(20) unique)"""

    try:
        with connect(__DB_FILENAME) as conn:
            cur = conn.cursor()  # an object capable of executing SQL commands
            cur.execute(sql_cmd)
            print('The table CUSTOMERS created successfully.')
    except DatabaseError as err:
        print(f'There was an error - {err}')


def add_new_customer():
    print('Enter new customer details: ')
    name = input('Name : ')
    email = input('Email: ')
    phone = input('Phone: ')
    sql_cmd = 'insert into customers(name, email, phone) values (?, ?, ?)'
    try:
        with connect(__DB_FILENAME) as conn:
            cur = conn.cursor()  # an object capable of executing SQL commands
            cur.execute(sql_cmd, (name, email, phone))
            new_id = cur.lastrowid
            print(f'New record to the CUSTOMERS table added successfully. ID: {new_id}')
    except DatabaseError as err:
        print(f'There was an error - {err}')


def list_all_customers():
    try:
        with connect(__DB_FILENAME) as conn:
            cur = conn.cursor()  # an object capable of executing SQL commands
            cur.execute('select * from customers')
            print('-'*75)
            print('ID   Name                 Email                           Phone          ')
            print('-'*75)
            for rec in cur.fetchall():
                print('%-5d%-21s%-32s%-15s' % rec)
            print('-'*75)

    except DatabaseError as err:
        print(f'There was an error - {err}')


def search_customer_by_id():
    try:
        c_id = int(input('Enter customer id to search: '))
        sql_cmd = 'select * from customers where id = ?'
        try:
            with connect(__DB_FILENAME) as conn:
                cur = conn.cursor()  # an object capable of executing SQL commands
                cur.execute(sql_cmd, (c_id, ))
                rec = cur.fetchone()
                if rec is None:
                    print(f'No data found for id {c_id}')
                else:
                    print("""Customer data found: 
        ID        : %d
        Name      : %s
        Email id  : %s
        Phone #   : %s""" % rec)

        except DatabaseError as err:
            print(f'There was an error - {err}')
    except ValueError:
        print('Customer ID must be a number.')


def display_and_accept(field, value):
    temp_input = input(f'Enter {field}: [{value}] ')
    return temp_input if temp_input else value

def edit_customer_data():
    try:
        c_id = int(input('Enter customer id to edit: '))
        with connect(__DB_FILENAME) as conn:
            cur = conn.cursor()
            cur.execute('select * from customers where id = ?', (c_id, ))
            rec = cur.fetchone()
            if rec is None:
                print(f'No customer data found for id {c_id}')
                return
            _, name, email, phone = rec

            name = display_and_accept('name', name)
            email = display_and_accept('email address', email)
            phone = display_and_accept('phone number', phone)

            rec = (name, email, phone, c_id)
            sql_cmd = 'update customers set name=?, email=?, phone=? where id=?'
            cur.execute(sql_cmd, rec)
            print('Customer data updated successfully!')
    except ValueError:
        print('Invalid value for id. Must be a number.')
    except DatabaseError as err:
        print(f'There was an error - {err}')


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
                create_customers_table()
            elif choice == 2:
                add_new_customer()
            elif choice == 3:
                list_all_customers()
            elif choice == 4:
                search_customer_by_id()
            elif choice == 5:
                edit_customer_data()
            elif choice == 6:
                print('Thank you, have a nice day!')
                break
            else:
                print('Invalid choice. Please try again')
        except ValueError:
            print('Invalid choice. Please try again')