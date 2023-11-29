"""
Example of creating `abstract` classes with `abstract` methods
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):  # class Shape is abstract, and cannot be instantiated
    @abstractmethod
    def print_area(self):
        # this is an abstract method
        # no method body is allowed here
        # subclasses must override and implement this method
        # else, they become abstract class, and cannot be instantiated
        pass


class Circle(Shape):
    def __init__(self, radius=1.0):
        self.radius = radius

    # override the inherited abstract method
    def print_area(self):
        area = math.pi * (self.radius**2)
        print(f'area of circle with radius of {self.radius} is {area}')

class Rectangle(Shape):
    def __init__(self, side1=1.0, side2=1.0):
        self.side1 = side1
        self.side2 = side2

    # override the inherited abstract method
    def print_area(self):
        area = self.side1 * self.side2
        print(f'area of a rectangle with sides {self.side1} and {self.side2} is {area}')


# example of a polymorphic method
def process_shape(s1: Shape) -> None:
    if not isinstance(s1, Shape):
        raise TypeError(f'Expected a Shape object, but got {type(s1)}')

    print('area of the given shape is:')
    s1.print_area()


if __name__ == '__main__1':
    c1 = Circle(1.2)
    r1 = Rectangle(1.2, 3.5)
    process_shape(c1)
    process_shape(r1) 
    process_shape(100)  # raises TypeError
