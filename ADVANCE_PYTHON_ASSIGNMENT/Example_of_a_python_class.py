'''
    How to Define a Class in Python? What Is Self? Give An Example Of
    A Python Class. 
'''

'''
Class: In python, you can define a class using the 'class' keyword.
Self: The self keyword is used as the first parameter in the method definitions inside a class.
      It represents the instance of the object and allows you to access its attributes and methods. 
'''

# Create class
class Person:

    # Dunder method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create function name of introduce 
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# create an object of Person class
person1 = Person("Kajal", 30)
person2 = Person("Ruchi", 25)

# print result and calling methods
print(f"Person 1: {person1.name}, {person1.age} years old")
print(f"Person 2: {person2.name}, {person2.age} years old")

person1.introduce()  
person2.introduce()  
