"""
Example of a polymorphic method
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self):
        self._data = 100

    @abstractmethod
    def shape_name(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def author_info(self):
        print('Created by Vinod <vinod@vinod.co> https://vinod.co')


class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius
        super().__init__()

    def shape_name(self):
        return 'Circle'

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, side1=1, side2=1):
        self.side1 = side1
        self.side2 = side2
        super().__init__()

    def shape_name(self):
        return 'Rectangle'

    def area(self):
        return self.side1 * self.side2

    def author_info(self):
        print(f'_data inherited from base class is {self._data}')
        print('Created by John Doe <johndoe@xmpl.com>')


def process_shape(shape: Shape):
    print(f'Got an object of type {type(shape)}')
    if not isinstance(shape, Shape):
        raise TypeError('this method takes an object of Shape class only')
    print(f'Name of the shape received is {shape.shape_name()}')
    print(f'Area of this shape is {shape.area()}')
    shape.author_info()
    print('-'*50)


def main():
    # s1 = Shape()
    c1 = Circle(1.2)
    r1 = Rectangle(1.2, 2.3)

    process_shape(c1)  # c1 is an instanceof --> Circle, Shape, object
    process_shape(r1)  # r1 is an instanceof --> Rectangle, Shape, object
    # process_shape('vinod')  # 'vinod' is an instanceof --> str, object
    # process_shape(123)  # 123 is an instanceof --> int, object


if __name__ == '__main__':
    main()
