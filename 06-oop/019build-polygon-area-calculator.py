# Objects-Oriented Programming (OOP)
    # OOP and Encapsulation
    # Inheritance and Polymorphism
    # Abstraction
#019 Certification Project: Build a Polygon Area Calculator

import math

class Rectangle():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, value):
        if value <= 0: raise ValueError('Width must be positive.')
        self.width = value
    def set_height(self, value):
        if value <= 0: raise ValueError('Height must be positive.')
        self.height = value
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2*(self.width + self.height)
    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def __str__(self) -> None:
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        output = ''
        for _ in range(0, self.height):
            output += '*' * self.width
            output += '\n'
        return output

    def get_amount_inside(self, other_figure):
        b = self.width // other_figure.width
        h = self.height // other_figure.height
        tot = b * h
        return tot

class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        if side <= 0: raise ValueError('Side must be positive.')
        self.width = side
        self.height = side
        self.side = side

    def set_width(self, width):
        self.set_side(width) # <==> if value <= 0: raise ValueError('Width must be positive.')

    def set_height(self, height):
        self.set_side(height)

    def __str__(self) -> None:
        return f'Square(side={self.side})'

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
