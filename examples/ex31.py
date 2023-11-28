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
        return f'Book(title="{self.title}", author="{self.author}", price={self.price}, page_count={self.page_count})'

    def print_info(self):
        print(f"""Book details:
        Title      : {self.title}
        Author     : {self.author}
        Price      : Rs.{self.price}
        No.of pages: {self.page_count}""")


def main():
    b1 = Book(title='Let us C', author='Y Kanitkar', price=499, page_count = 129)
    b2 = Book(author='John Doe', title='Python Unleashed')
    b1.print_info()
    b2.print_info()
    print(b1)  # print(b1.__str__())
    print(b2)


if __name__ == '__main__':
    main()
