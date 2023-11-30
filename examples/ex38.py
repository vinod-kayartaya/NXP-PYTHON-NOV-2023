"""
Example of using `threading` module in python
"""
from threading import Thread


def some_task(limit: int, message: str) -> None:
    for i in range(limit):
        print(f'{message} - {i}')
        if i == 19:
            raise ValueError('this is an error!')


def main():
    # some_task(15, 'this is the first task')
    # some_task(20, 'hello from second task')
    t1 = Thread(target=some_task, args=(15, 'this is the first task'))
    t2 = Thread(target=some_task, args=(20, 'hello from second task'))

    t1.start()
    t2.start()

    for i in range(100):
        print(f'this message is coming from main() and i is {i}')


if __name__ == '__main__':
    main()
