class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f"informacja o kształcie {self.x} {self.y}")

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    # def __str__(self):
    #     return f"Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})"

class Circle(Shape):
    def __init__(self,x, y,r, color):
        super().__init__(x, y, color)
        self.r = r