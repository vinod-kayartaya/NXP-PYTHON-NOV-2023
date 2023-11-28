class Book:
    # override the default __init__() given by Python
    def __init__(self, **kwargs):
        print(kwargs)
        self.title = kwargs.get('title')
        self.author = kwargs.get('author')
        self.price = kwargs.get('price', 0.0)
        self.page_count = kwargs.get('page_count', 0)

    # override the default __str__() method given by Python
    def __str__(self):
        # returns a textual representation of the invoking object (i.e, `self`)
        _title = None if self.title is None else f'"{self.title}"'
        _author = None if self.author is None else f'"{self.author}"'
        return f'Book(title={_title}, author={_author}, price={self.price}, page_count={self.page_count})'

    def print_info(self):
        print(f"""Book details:
        Title      : {self.title}
        Author     : {self.author}
        Price      : Rs.{self.price}
        No.of pages: {self.page_count}""")


def main():
    b1 = Book(title='Let us C', author='Y Kanitkar', price=499, page_count = 129)
    b2 = Book()
    b2.price = 20000000
    b2.page_count = -123
    b2.title = ''
    b2.author = 1.234

    b1.print_info()
    b2.print_info()
    print(b1)  # print(b1.__str__())
    print(b2)


if __name__ == '__main__':
    main()
