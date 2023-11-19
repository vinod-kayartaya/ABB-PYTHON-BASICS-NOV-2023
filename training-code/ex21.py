"""
Create class called `Person`, objects of which can be customizable with different values (data)
"""
from my_utils import dir2


class Person:
    def __init__(self, **kwargs):
        print('Person.__init__() called')
        # using the setter properties, validation is achieved
        self.fname = kwargs.get('fname', None)
        self.lname = kwargs.get('lname', None)
        self.email = kwargs.get('email', None)
        self.age = kwargs.get('age', 18)

    def print_info(self):
        print(f'Name   = {self.__fname} {self.__lname}')
        print(f'Email  = {self.__email}')
        print(f'Age    = {self.__age} years')

    # getter property (aka accessor or readable property)
    @property
    def fname(self):
        return self.__fname

    @property
    def lname(self):
        return self.__lname

    @property
    def email(self):
        return self.__email

    @property
    def age(self):
        return self.__age

    @property
    def fullname(self):
        return self.__fname + ' ' + self.__lname

    @staticmethod
    def __validate(value):
        if type(value) is not str:
            raise TypeError('value must be a string')
        if value.strip() == '':
            raise ValueError('value cannot be blank')
        if len(value.strip()) > 10:
            raise ValueError('value cannot exceed 10 letters')

    @fname.setter
    def fname(self, value):
        if value is None: return
        Person.__validate(value)
        self.__fname = value.capitalize()

    @lname.setter
    def lname(self, value: str):
        if value is None: return
        self.__validate(value)
        self.__lname = value.capitalize()

    @age.setter
    def age(self, value: int):
        if value is None: return
        if type(value) is not int:
            raise TypeError('age must be an integer')
        if value < 1 or value > 120:
            raise ValueError('age must be between 1 and 120')
        self.__age = value

    @email.setter
    def email(self, value: str):
        if value is None: return
        if type(value) is not str:
            raise TypeError('email must be a string')
        self.__email = value.lower()

    # override the inherited __str__ magic method to get a textual representation of the object
    def __str__(self):
        return f'Person(fname=\'{self.__fname}\', lname=\'{self.__lname}\', age={self.__age}, email=\'{self.email}\')'


def main():
    p1 = Person(fname='VIJAY', lname='kumar', age=44, email='VIJAY.KUMAR@EXAMPLE.COM')
    p2 = Person(fname='VINOD', lname='KUMAR', email='VINOD@VINOD.CO', age=50)
    print(p1)
    print(p2)
    print(dir(p1))


def main_3():
    p1 = Person()
    p1.print_info()

    p1.fname = 'Vinod'
    p1.lname = 'Kumar'
    p1.email = 'vinod@vinod.co'
    p1.age = 50
    p1.print_info()


def main_2():
    p1 = Person(fname='Vinod', lname='Kumar', email='vinod@vinod.co', age=50)
    p1.print_info()
    print(f'p1.fname is {p1.fname}')
    print(f'p1.lname is {p1.lname}')
    print(f'p1.age is {p1.age}')
    print(f'p1.email is {p1.email}')
    print(f'p1.fullname is {p1.fullname}')


def main_1():
    p1 = Person()
    p2 = Person(fname='Vinod', lname='Kumar', email='vinod@vinod.co', age=50)
    print(dir(p1))
    print(dir2(p2))

    p1.print_info()
    print('-'*50)
    p2.print_info()
    print('-'*50)
    p1.__fname = False
    p1.__lname = True
    p1.__age = -500
    p1.__email = 'suresh'
    p1.print_info()


if __name__ == '__main__':
    main()
