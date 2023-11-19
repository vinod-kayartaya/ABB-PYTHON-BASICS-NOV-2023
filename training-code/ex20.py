"""
Example for creating classes and objects
"""
from my_utils import dir2


class Car:
    def __init__(self):
        print(f'A Car instance is created! and id(self) is {id(self)}')
        self.make = None
        self.model = None
        self.color = None
        self.horse_power = None
        self.transmission_type = None

    def print_info(self):
        # `self` is the reference to the invoking object
        # c1.print_info() --> `self` is `c1`
        # c2.print_info() --> `self` is `c2`
        print(f'The car info will be printed here and id(self) is {id(self)}')


def main():
    c1 = Car()
    print(f'id(c1) is {id(c1)}')
    # 1. python creates an object space
    # 2. python invokes the __init__() method of the class by supplying the reference to the newly created object space
    #    generally received using a variable called `self`
    # 3. python then returns the reference to the newly constructed object (which is same as `self`)
    # Since we have access to the newly constructed object space in the __init__ method, we can add new attributes to
    # the object
    c2 = Car()
    print(f'id(c2) is {id(c2)}')

    c3 = Car()
    print(f'id(c3) is {id(c3)}')

    print(f'type of c1 is {type(c1)}')
    print(f'all attributes in c1 are {dir(c1)}')
    print(f'attributes from class `object` {dir(object)}')
    print(f'non-dunder attributes in c1 are {dir2(c1)}')
    print(f'c1.__dict__ is {c1.__dict__}')

    c1.print_info()  # Car.print_info(c1)
    c2.print_info()
    c3.print_info()


if __name__ == '__main__':
    main()
