'''
    Explain Inheritance in Python with an example? What is init? Or What
    Is A Constructor In Python? 
'''

'''
Inheritance:  Inheritance relationship defines the classes that inherit from other classes as derived,
              subclass, or sub-type classes. Base class remains to be the source from which a subclass inherits. 
'''

# Example of Inheritance:

# Create class named of calculation1
class Calculation1:  
    def Addition(self,a,b):  
        return a+b;  

# Create class named of calculation2
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  

# Create class named of calculation3
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  

# Create object of class derived
d = Derived()  

# Print results
print(d.Addition(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  

'''
Init: In Python, __init__ is a special method, often referred to as the "initializer" or "constructor." 
It is automatically called when an instance of a class is created. 
The primary purpose of __init__ is to initialize the attributes of the object.
'''

'''
Constructor: In Python, a constructor is a special method named __init__. 
It is a type of method that is automatically called when an object is created from a class. 
The primary purpose of a constructor is to initialize the attributes of the object.
'''

