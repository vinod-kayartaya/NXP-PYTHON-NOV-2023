"""
Exploring the `list` class.

The `list` class has these attributes:
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
'remove', 'reverse', 'sort'
"""


def main():
    data = [10, 20, 30, 40, 11, 28, 48, 29, 58]
    print(data)
    data.append(12)
    print(data)
    data.extend([11, 12, 13])
    print(data)
    data.append([99, 88, 77])  # appends the entire list as a single element
    print(data)
    data += [12, 32, 45]  # same as extend()
    print(data)
    # nums += 100  # error, RHS of += must be a list
    # print(nums)
    data_len = len(data)
    print(f"there are {data_len} elements in `data`")
    data += 'vinod'  # 'vinod' is equivalent of ['v', 'i', 'n', 'o', 'd']
    print(data)
    data += ['vinod']
    print(data)
    n = 12
    print(f'{n} appears {data.count(n)} in the list `data`')
    print(f'{n} in data is {n in data}')

    print(f'index of {n} in `data` is {data.index(n)}')
    data.insert(0, 9)  # prepend an element to the list
    data.insert(100000, 100)  # appends to the list (assuming there are less than 100000 elements)
    data.insert(-1000, 111)
    print(data)

    # pop([index]) removes the last element if index is not specified, else the element at given index
    # remove(value) removes the value from the given list
    n = data.pop()  # returns the last element from `data` and removes the same in the collection
    print(f'{n} is the popped element, and data is {data}')
    sub_list = [99, 88, 77]
    if sub_list in data:
        idx = data.index(sub_list)
        n = data.pop(idx)
        print(f'after removing, {n}, data is {data}')

    if 'vinod' in data:
        data.remove('vinod')
        print(f'after removing "vinod", data is {data}')

    for ch in 'vinod':
        data.remove(ch)

    data.reverse()
    print(f'after reversing, data is {data}')

    data.sort()
    print(f'after sorting, data is {data}')


if __name__ == '__main__':
    main()
