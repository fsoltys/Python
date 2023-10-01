class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def dimensions(self):
        print(f"Ta figura ma wymiary {self.a} x {self.b}")


class Square(Rectangle):
    def __init__(self, a):
        self.a = self.b = a


rectangle = Rectangle(15, 20)
print(f"Prostokat o podanych wymiarach ma pole {rectangle.area()}")
rectangle.dimensions()
square = Square(6)
print(f"Kwadrat o podanych wymiarach ma pole {square.area()}")
square.dimensions()
