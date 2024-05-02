import math


class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f"Shape: color={self.color}, center=({self.x}, {self.y})")

    def distance(self, other_shape):
        dx = self.x - other_shape.x
        dy = self.y - other_shape.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return f"tutaj jest string"

shape1 = Shape(2, 5, "red")
shape2 = Shape(10, 20, "green")
shape1.describe()
shape2.describe()
print(shape1.distance(shape2))