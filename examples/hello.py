"""
This is an example module.

Has a function and a variable.

@author Vinod Kumar K
"""
my_name = 'Vinod'


def greet():
    """
    Prints a greeting message

    This method takes no parameter and simple prints a nice
    greeting message. This method depends on the global
    variable `my_name`. Try changing the value of `my_name` from
    the CLI.
    """
    print('Hello friend, from', my_name)
    print('Welcome to Python training.')   


greet()