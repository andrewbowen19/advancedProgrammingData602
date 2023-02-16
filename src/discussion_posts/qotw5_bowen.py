# QOTW 5
# Andrew Bowen
# DATA602
from math import pi

class StringReverser:

    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        '''Sets string attr to reverse order'''
        self.string = self.string[-1::-1]


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        self.perimeter = 2 * pi * self.radius

    def calculate_area(self):
        self.area = pi * self.radius ** 2

if __name__ == "__main__":
    # Test call to reverse string order
    sr = StringReverser("hello.py")
    sr.reverse_string()

    print(sr.string)

    # Test calls of Circle class
    c = Circle(5)
    c.calculate_area()
    c.calculate_perimeter()

    print(f"Area: {c.area}")
    print(f"Perimeter: {c.perimeter}")