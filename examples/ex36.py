"""
No overload here!!!
"""
class Test:

    def say_hello(self):
        print('Hello, world!')

    def say_hello(self, name, city):
        print(f'{name} from {city} says hello')


if __name__ == '__main__':
    t1 = Test()
    t1.say_hello()
    t1.say_hello('Vinod', 'Bangalore')