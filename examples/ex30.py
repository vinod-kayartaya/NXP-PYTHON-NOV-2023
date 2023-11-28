class Book:
    # data shared across all objects of Book class
    book_types = ['programming', 'fiction', 'drama']
    title = None


def main():
    b1 = Book()
    b2 = Book()

    print(f'b1.book_types is {b1.book_types}, b1.title = {b1.title}')
    print(f'b2.book_types is {b2.book_types}, b2.title = {b2.title}')

    b1.book_types.append('comedy')
    b1.title = 'Let us C'  # new attribute in b1
    b1.author = 'Y Kanitkar'  # new attribute in b1
    print(f'b1.book_types is {b1.book_types}, b1.title = {b1.title}')
    print(f'b2.book_types is {b2.book_types}, b2.title = {b2.title}')
    print(f'b1 is {b1}')


if __name__ == '__main__':
    main()