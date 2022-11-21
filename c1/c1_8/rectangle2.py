from figure import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

print(rect1.get_area())
print(rect2.get_area())

square1 = Square(5)
square2 = Square(10)

print(square1.get_area_square(), square2.get_area_square())

figures = [rect1, rect2, square1, square2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

circle1 = Circle(1)
circle2 = Circle(2)

print(circle1.get_area())
print(circle2.get_area())
