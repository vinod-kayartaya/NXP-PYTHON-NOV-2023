"""
Understand the use of list.copy() method.


"""
import json


def main():
    data1 = [100, 'vinod', [10, 20], False]
    data2 = data1  # another reference to the same list object (not copied)
    data1.append(200)
    print(f'data1 is {data1}')
    print(f'data2 is {data2}')

    data3 = data1.copy()  # shallow copy
    data1.append(300)
    print(f'data1 is {data1}')
    print(f'data2 is {data2}')
    print(f'data3 is {data3}')
    data2[1] = 'kumar'
    print()
    print(f'data1 is {data1}')
    print(f'data2 is {data2}')
    print(f'data3 is {data3}')

    data1[2].append(30)
    print()
    print(f'data1 is {data1}')
    print(f'data2 is {data2}')
    print(f'data3 is {data3}')

    # deep copy using `json` module methods
    data4 = json.loads(json.dumps(data1))
    data1[2].append(40)
    print()
    print(f'data1 is {data1}')
    print(f'data2 is {data2}')
    print(f'data3 is {data3}')
    print(f'data4 is {data4}')


if __name__ == '__main__':
    main()
