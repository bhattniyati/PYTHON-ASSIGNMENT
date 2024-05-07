'''
    How many except statements can a try-except block have? Name Some
    built-in exception classes: 
'''

'''
A try-except block in Python can have multiple except clauses to handle different types of exceptions. 
There is no strict limit on the number of except statements you can have. You can handle various exceptions in different except blocks based on your requirements.
'''

'''
Some common built-in exception classes in Python include:
1. ValueError
2. ZeroDivisionError
3. FileNotFoundError
4. KeyError
'''

# Example of try-except block:

try:
    # Code that may raise an exception
    result = x / y

except ValueError:
    # Handle ValueError
    print("Caught a ValueError")

except ZeroDivisionError:
    # Handle ZeroDivisionError
    print("Caught a ZeroDivisionError")

except Exception as e:
    # Handle other exceptions
    print(f"Caught an exception: {e}")

