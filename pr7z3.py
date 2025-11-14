class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2

def print_area(shape: Shape):
    print(shape.area())
shapes = [Square(4), Circle(3)]
for s in shapes:
    print_area(s)
