'''
    What relationship is appropriate for Course and Faculty?
'''
'''
The appropriate relationship between "Course" and "Faculty" in Python can be modeled as an association. 
An association represents a relationship between two classes, 
indicating that instances of one class are related to instances of another class.
'''

# Craete class name of faculty
class Faculty:
    
    # Dunder method
    def __init__(self,name,department):
            self.name = name
            self.department = department
    
    # Dunder method return string format
    def __str__(self):
          return f"Name: {self.name}, Department: {self.department}"

# Create class name of Course
class Course:
      
      # Dunder method
      def __init__(self,title,faculty):
            self.title = title
            self.faculty = faculty

      # Dunder method return string format
      def __str__(self):
            return f"Course: {self.title}, Faculty: {self.faculty}"
      
# Create an object class name of faculty
f1= Faculty("Ruchi Maurya", "Computer Science")

# Create an object class name of course and pass argument in faculty of object
c1= Course("Python Programming",f1)

# print result
print(c1)