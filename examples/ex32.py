"""
Example for encapsulation.

A single underscore prefix is used for denoting `protected` and
a double underscore prefix is used for denoting `private` (in other languages)
"""


class Book:
    # override the default __init__() given by Python
    def __init__(self, **kwargs):
        # now we are using the setter property for the assignments which will take care of validations
        self.title = kwargs.get('title')
        self.author = kwargs.get('author')
        self.price = kwargs.get('price')
        self.page_count = kwargs.get('page_count')

    # override the default __str__() method given by Python
    def __str__(self):
        # returns a textual representation of the invoking object (i.e, `self`)
        _title = None if self.__title is None else f'"{self.__title}"'
        _author = None if self.__author is None else f'"{self.__author}"'
        return f'Book(title={_title}, author={_author}, price={self.__price}, page_count={self.__page_count})'

    def print_info(self):
        print(f"""Book details:
        Title      : {self.__title}
        Author     : {self.__author}
        Price      : Rs.{self.__price}
        No.of pages: {self.__page_count}""")

    # getter or accessor method. (readable property called `title`)
    @property
    def title(self):
        return self.__title.upper()

    # setter or mutator method (writable property called `title`)
    @title.setter
    def title(self, value):
        if value is not None and type(value) is not str:
            raise TypeError('Invalid type for `title`. Must be a str.')

        if value is not None and len(value) > 15:
            raise ValueError('`title` must be less than or equals to 15 letters')

        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if value is not None and type(value) is not str:
            raise TypeError('Invalid type for `author`. Must be a str.')
        self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value is not None and type(value) not in (int, float):
            raise TypeError('Invalid type for price. Must be one of int or float')

        self.__price = value

    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, value):
        if value is not None and type(value) is not int:
            raise TypeError('Invalid type for price. Must be int')
        if value is not None and value <= 0:
            raise ValueError('page count must be > 0')
        self.__page_count = value


def main():
    b1 = Book(title='Python cookbook', author='Vinod Kumar', price=200, page_count=100)
    print(f'b1.title is {b1.title}')  # getter for `title` is called here
    print(b1)
    b1.print_info()
    # print(f'b1.__price is {b1.__price}')  # gives an error since __price is a hidden variable
    b2 = Book()
    b2.print_info()
    b2.title = 'Let us C'  # setter for `title` is called here. b2 is the `self`, RHS is given as `value`
    b2.author = 'Y Kanitkar'
    b2.price = 599.9
    b2.page_count = 120
    b2.print_info()
    b3 = Book(title='Python Flask', author='Ramesh Kumar', price=1599, page_count=902)
    b3.print_info()


if __name__ == '__main__':
    main()
