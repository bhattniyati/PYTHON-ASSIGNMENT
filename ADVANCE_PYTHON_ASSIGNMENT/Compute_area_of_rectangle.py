'''
    Write a Python class named Rectangle constructed by a length and -
    width and a method which will compute the area of a rectangle 
'''
# Create class named of rectangle
class Rectangle:

    # Dunder method
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Create function named of area
    def area(self):
        area = self.length * self.width
        return area

# Create object of Rectangle class and with 2 arguments.
rectangle= Rectangle(length=5, width=3)

# Print result
print(f"Length: {rectangle.length}")
print(f"Width: {rectangle.width}")
print(f"Area: {rectangle.area()}")
