"""
An example to read inputs from the user
"""


user_name = input('What is your name? ')
user_city = input('Where are your from? ')

print('Hello ' + user_name + ', how is weather in ' + user_city + '?')
print('Hello %s, how is weather in %s?' % (user_name, user_city))
print('hello {}, how is weather in {}?'.format(user_name, user_city))
print(f'Hello {user_name}, how is weather in {user_city}?')
