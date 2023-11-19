"""
Example of understanding inheritance in Python
"""
from ex21 import Person
from my_utils import dir2


class Student(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('Student.__init__() called')
        self.subject = kwargs.get('subject', None)
        self.gpa = kwargs.get('gpa', None)

    # override the inherited method
    def print_info(self):
        super().print_info()
        print(f'Subject= {self.subject}')
        print(f'GPA    = {self.gpa}')

    # override the __str__ magic method too
    def __str__(self):
        return (f"Student(fname='{self.fname}', lname='{self.lname}', age={self.age}, email='{self.email}', "
                f"subject='{self.subject}', gpa={self.gpa})")

    # magic comparison methods
    def __lt__(self, value):
        if type(value) not in (int, Student):
            raise TypeError('value must be either int or Student object')
        if type(value) is int:
            return self.age < value
        if type(value) is Student:
            return self.gpa < value.gpa

    def __gt__(self, value):
        if type(value) not in (int, Student):
            raise TypeError('value must be either int or Student object')
        if type(value) is int:
            return self.age > value
        if type(value) is Student:
            return self.gpa > value.gpa

    def __iadd__(self, value):
        if type(value) not in (int, str):
            raise TypeError('value must be either int or str')
        if type(value) is int:
            self.age += value
        if type(value) is str:
            self.subject += value
        return self

    def __add__(self, value):
        if type(value) is int:
            return self.age + value
        raise TypeError('value must be an integer')


def main():
    s1 = Student(fname='Rohit', lname='Kumar', age=18, email='rohit.kumar@xmpl.com', subject='Maths', gpa=4.1)
    s2 = Student(fname='Rajesh', lname='Rao', age=18, email='rajesh.rao@xmpl.com', subject='Physics', gpa=4.1)
    print(dir2(s1))
    print(s1.__dict__)
    s1.print_info()
    print(s1)

    if s1 < 20:  # s1.__lt__(20) --> must compare the age of s1 with 20
        print(f'{s1.fullname} is younger than 20 years')
    else:
        print(f'{s1.fullname} is older than 19 years')

    if s1 < s2:  # s1.__lt__(s2)  --> compare s1.gpa with s2.gpa
        print(f'{s1.fullname} scored less than {s2.fullname}')
    elif s1 > s2:  # s1.__gt__(s2)
        print(f'{s1.fullname} scored more than {s2.fullname}')
    else:
        print(f'{s1.fullname} scored same as {s2.fullname}')

    s1 += ' (algebra)'  # we want the RHS to be appended to the subject
    s1 += 5  # we want to RHS to be added to the age; s1.age changed to 23

    print('-'*80)
    s1.print_info()
    print('-'*80)

    print(s1+5)  # prints 23, but s1.age remains 18
    s1.print_info()

    # +=  is implemented by a method __iadd__
    # __isub__, __imul__, __idiv__, __imod__,
    # also, check out: __add__ __sub__ __mul__ __div__ __mod__ etc


if __name__ == '__main__':
    main()
