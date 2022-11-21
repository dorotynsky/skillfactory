class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.height}, {self.width}'

    def get_area(self):
        return self.height * self.width


rect1 = Rectangle(10, 20, 100, 200)

print(rect1)
print(f'Area: {rect1.get_area()}')
