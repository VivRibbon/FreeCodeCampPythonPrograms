class Rectangle:
    """The rectangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        """Set width function"""
        self.width = width

    def set_height(self, height):
        """Set height function"""
        self.height = height

    def get_area(self):
        "Return area"
        return self.width * self.height

    def get_perimeter(self):
        """Return perimeter"""
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        """Return diagonal"""
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        """Return visualization of shape in console"""
        return (("*" * self.width) + "\n") * self.height

    def get_amount_inside(self, shape):
        """Return number of times passed shape can fit in self."""
        self.area = self.width * self.height
        shape.area = shape.width * shape.height
        return round((self.area / shape.area))

class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height


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
