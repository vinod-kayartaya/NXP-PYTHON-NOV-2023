"""
Example of an entry point method
"""


print(f'value of __name__ in ex03, is {__name__}')


def greet():
    print('Hello and welcome to Python training.')


def say_hello():
    user_name = input('Enter your name: ')
    print(f'Hello, {user_name}!')


# execute the following block of code only if
# the current script is being run
# and not being imported
if __name__ == '__main__':
    say_hello()
