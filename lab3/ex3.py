class Shape:

    def __new__(cls, sides, *args, **kwargs):
        if sides == 3:
            return Triange(*args, **kwargs)
        elif sides == 4:
            return Square(*args, **kwargs)


class Square:

    def __init__(self, length):
        print('It is a square')
        self.length = length

    def area(self):
        return self.length ** 2


class Triange:

    def __init__(self, **kwargs):
        print('It is a triangle')
        self.base = kwargs.get('base')
        self.height = kwargs.get('height')

    def area(self):
        return (self.base * self.height) / 2


square = Shape(4, 5)
triangle = Shape(3, 4, 5)

print(square.area())
print(triangle.area())
