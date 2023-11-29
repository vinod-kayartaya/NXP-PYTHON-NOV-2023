"""
Example of using inheritance in Python
"""
from my_utils import dir2


class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')

    def print(self):
        print(f'Name   = {self.name}')
        print(f'Email  = {self.email}')


class Employee(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.salary = kwargs.get('salary')
        self.department = kwargs.get('department')

    # override the inherited method from Person class
    # hides the visibility of the super class method
    def print(self):
        super().print()
        print(f'Salary = {self.salary}')
        print(f'Dept   = {self.department}')

    def __del__(self):
        print('this is the last method to be called by an object, automatically')


if __name__ == '__main__':
    p1 = Person(name='Vinod', email='vinod@vinod.co')
    p1.print()
    print(dir2(p1))
    e1 = Employee(name='Jacob', salary=23400, department='ADMIN', email='jacob@xmpl.com')
    print(dir(e1))
    e1.print()
    # if this is the last line in this `if` block, then e1.__del__() will be called by python automatically

# e1 does not exist here
