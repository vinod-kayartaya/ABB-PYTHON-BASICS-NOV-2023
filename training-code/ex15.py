"""
Example to understand and use `dict` type

A dict object represents a collection of values identified using keys.
A key in a dict must be a unique and immutable.
If a key is already present, and you assign a value to the key, it will overwrite.
"""


def main():
    p1 = dict(fname='Vinod', lname='Kumar', age=50, married=True)
    print(f'p1 is {p1}')

    key = input('Enter the key to search: ')
    # print(f'p1[key] is {p1[key]}')
    # p1[key] may raise an exception called KeyError, if the key is not found in the dict

    val = p1.get(key)
    if val is not None:
        print(f'value corresponding to the key given is {val}')
    else:
        print(f'either the key is not there or the value is None')

    p1['email'] = 'vinod@vinod.co'
    print(f'p1 is {p1}')
    del p1['age']
    print(f'p1 is {p1}')
    p1['lname'] = 'Kayartaya'
    print(f'p1 is {p1}')
    p1[0] = 'Bangalore'
    print(f'p1 is {p1}')
    # access all the keys in the dict
    for key in p1.keys():
        print(key)
    # access all the values in the dict
    for val in p1.values():
        print(val)
    # access both key and corresponding value at the same time
    for item in p1.items():
        print(item)
    for key, val in p1.items():
        print(f'{key} --> {val}')


if __name__ == '__main__':
    main()
