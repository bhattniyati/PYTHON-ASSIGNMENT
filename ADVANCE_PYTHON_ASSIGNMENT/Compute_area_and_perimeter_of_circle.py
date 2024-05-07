'''
    Write a Python class named Circle constructed by a radius and two -
    methods which will compute the area and the perimeter of a circle. 
'''

# Create class named of Circle
class Circle():

    # Dunder method
    def __init__(self,r):
        self.radius= r

    # Create function named of area
    def area(self):
        return self.radius **2*3.14
    
    # Create function named of perimeter
    def perimeter(self):
        return 2*self.radius*3.14

# Create object of class Circle
NewCircle= Circle(8)

# print area
print(NewCircle.area())

# print perimeter
print(NewCircle.perimeter())
