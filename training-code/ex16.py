import json


def main():
    p1 = dict(fname='Vinod', lname='Kumar', phones=['9731424784'])
    p2 = p1  # 2 references to 1 dict object
    print(f'p1 is {p1}')
    print(f'p2 is {p2}')

    p1['email'] = 'vinod@vinod.co'
    print(f'p1 is {p1}')
    print(f'p2 is {p2}')

    p3 = p1.copy()  # creates a shallow copy
    p1['phones'].append('9844083934')  # will affect p3, since 'phones' is a mutable
    p1['email'] = 'vinod@kwit.com'  # will not affect p3, since 'email' is a str, which is an immutable
    print(f'p1 is {p1}')
    print(f'p2 is {p2}')
    print(f'p3 is {p3}')

    # deep copy
    p4 = json.loads(json.dumps(p1))
    p1['phones'].append('8022266199')  # affects p2 and p3, but not p4 (since p4 is totally a new object)
    print(f'p1 is {p1}')
    print(f'p2 is {p2}')
    print(f'p3 is {p3}')
    print(f'p4 is {p4}')


if __name__ == '__main__':
    main()
