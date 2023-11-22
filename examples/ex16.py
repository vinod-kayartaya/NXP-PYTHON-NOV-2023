"""
Example to understand slice operations on a list object
"""


def main():
    data = [10, 20, 30, 40, 11, 28, 48, 29, 58, 28]
    print(f'the first element in data is {data[0]}')
    print(f'the third element in data is {data[2]}')
    print(f'the last element in data is {data[len(data)-1]}')
    print(f'the last element in data is {data[-1]}')
    print(f'the first element in data is {data[-len(data)]}')

    # slice operator allow us to access a sub-list from a list
    sublist = data[3:7]  # starting from index 3, (7-3) elements
    print(f'sublist is {sublist}')
    sublist = data[0:5]  # first 5 elements
    print(f'sublist is {sublist}')
    sublist = data[:5]  # first 5 elements
    print(f'sublist is {sublist}')
    sublist = data[6: len(data)]  # elements from index 6
    print(f'sublist is {sublist}')
    sublist = data[6: 100000]  # elements from index 6
    print(f'sublist is {sublist}')
    sublist = data[6:]  # elements from index 6
    print(f'sublist is {sublist}')
    sublist = data[6:-1]  # elements from index 6 excluding the last element
    print(f'sublist is {sublist}')

    # more slice operations
    # data[start=0: end=len: step=1]
    print(f'data[:] is {data[:]}')
    print(f'data[::] is {data[::]}')
    print(f'data[0:len(data):2] is {data[0:len(data):2]}')
    print(f'data[0::2] is {data[0::2]}')
    print(f'data[::2] is {data[::2]}')
    print(f'data[1::2] is {data[1::2]}')
    print(f'data[::-1] is {data[::-1]}')
    name = 'vinod'
    print(f'reverse of "{name}" is "{name[::-1]}"')

    filename = 'example_file.txt'
    basename = filename[:-4]
    print(f'filename is "{filename}" and basename is "{basename}"')


if __name__ == '__main__':
    main()
