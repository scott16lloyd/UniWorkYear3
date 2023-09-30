import copy

# Shape prototype


class Shape:
    def __init__(self, type, no_of_sides):
        self.type = type
        self.no_of_sides = no_of_sides

    def __str__(self):
        return f"The shape {self.type} has {self.no_of_sides} number of sides"


# Concrete prototypes
# Square prototype
class Square(Shape):
    def __init__(self, type, no_of_sides):
        super().__init__("Square", 4)

# Circle prototype


class Circle(Shape):
    def __init__(self, type, no_of_sides):
        super().__init__("Circle", 1)

# ShapeFactory


class ShapeFactory:
    def __init__(self, prototype):
        self.prototype = prototype

    def create_shape(self, type):
        new_shape = copy.deepcopy(self.prototype)
        new_shape.type = type
        return new_shape


# Main
if __name__ == "__main__":
    # Create prototype
    square_prototype = Square("Square", 4)
    circle_prototype = Circle("Circle", 1)

    # Circle factory
    circle_factory = ShapeFactory(circle_prototype)

    # Create Circles
    circle1 = circle_factory.create_shape("Circle")
    circle2 = circle_factory.create_shape("Circle")

    print("Circles:")
    print(circle1)
    print(circle2)

    # Square factory
    square_factory = ShapeFactory(square_prototype)

    # Create Squares
    square1 = square_factory.create_shape("Square")
    square2 = square_factory.create_shape("Square")

    print("Square:")
    print(square1)
    print(square2)
