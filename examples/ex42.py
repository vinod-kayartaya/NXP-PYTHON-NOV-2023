import requests


customers_url = 'http://localhost:4000/api/customers'


def add_new_customer():
    name = input('Enter name: ')
    email = input('Enter email: ')
    phone = input('Enter phone: ')
    c1 = dict(name=name, email=email, phone=phone)
    response = requests.post(customers_url, json=c1)
    if response.status_code == 201:
        print(f'New customer data POSTED - {response.json()}')


def get_all_customers():
    response = requests.get(customers_url)
    print(response.status_code)
    if response.status_code != 200:
        print('Server did not respond with status code 200')
        return
    customers = response.json()
    print('{:<5}{:<20}{:<50}{:<15}'.format('ID', 'Name', 'Email', 'Phone'))
    print('-'*90)
    for each_customer in customers:
        print('{:<5}{:<20}{:<50}{:<15}'.format(
            each_customer.get('id'),
            each_customer.get('name'),
            each_customer.get('email'),
            each_customer.get('phone'),
        ))


if __name__ == '__main__':
    # get_all_customers()
    add_new_customer()
