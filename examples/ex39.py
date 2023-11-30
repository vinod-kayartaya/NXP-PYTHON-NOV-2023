"""
Thread using a resource from the parent thread
"""
from threading import Thread


def thread_function(file):
    for each_line in file:
        if each_line == '\n':
            continue

        cells = each_line.split(',')
        if cells[0] == 'id':
            continue

        name = cells[1] + ' ' + cells[2]
        email = cells[4]
        phone = cells[5]
        print(name, email, phone, sep=', ')


def main():
    try:
        with open('customers.csv', 'rt') as file:
            t1 = Thread(target=thread_function, args=(file, ))
            print('File handling started!')
            t1.start()
            t1.join()  # wait until t1's task is completed
            print('File operation finished!')
        # file is closed here
    except OSError as err:
        print(f'There was an error - {err}')


if __name__ == '__main__':
    main()
