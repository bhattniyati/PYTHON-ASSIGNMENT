'''
    What relationship is appropriate for Student and Person? 
'''
'''
The appropriate relationship between "Student" and "Person" in Python is generally an inheritance relationship, 
where "Student" is a subclass (or derived class) of "Person." 
This relationship is based on the concept that a "Student" is a specialized type of "Person."
'''

# Craete class name of Person
class Person:

    # Dunder method
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # Create function name of display_info
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create class name of Student
class Student(Person):
    
    # Dunder method
    def __init__(self,name,age,student_id):

        # Use super method-- This function returns an object that represents the parent class.
        super().__init__(name,age)
        self.student_id = student_id

    # Craete function name of display_info
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

# Craete an Object class of Person
person_instance = Person("Ruchi", 25)

# Craete an Object class of Student
student_instance = Student("Kajal", 27, 105)

# Call method
person_instance.display_info()  
student_instance.display_info()