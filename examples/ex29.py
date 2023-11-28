"""
Example of creating a class and instances of the same.
"""


class Book:
    def __init__(self, title=None, author=None, price=None, page_count=None):
        # this method is automatically called by python, when an object is created.
        # `self` is a reference to the newly constructed object by python
        print(f'Book.__init__() called for {self}')
        self.title = title  # new attribute called `title` created in this object
        self.author = author
        self.price = price
        self.page_count = page_count

    def print_info(self):
        print(f"""Book details:
        Title      : {self.title}
        Author     : {self.author}
        Price      : Rs.{self.price}
        No.of pages: {self.page_count}""")


def main():
    b1 = Book('Let us C', 'Y Kanitkar', 499, 129)  # b1 is an object (or instance) of Book class.
    b2 = Book('Python complete reference', 'John Doe')

    # print(f'b1 is {b1} and id(b1) is {id(b1)} and type(b1) is {type(b1)}')
    # print(f'b2 is {b2} and id(b2) is {id(b2)} and type(b2) is {type(b2)}')

    # print(dir(b1))
    # print(dir(b2))

    print(f'b1\'s title is {b1.title}')
    print(f'b2\'s title is {b2.title}')

    b1.print_info()  # b1 is the invoking object; it will be automatically passed as the 1st arg
    Book.print_info(b1)
    b2.print_info()  # b2 is passed as the first argument implicitly


if __name__ == '__main__':
    main()
