'''
    How Do You Handle Exceptions With Try/Except/Finally In Python?
    Explain with coding snippets.

'''

'''
The try, except, and finally blocks to handle exceptions. 
The try block contains the code that might raise an exception, 
the except block contains the code to handle the exception,and
the finally block contains code that will be executed whether an exception is raised or not.

'''
try:
    
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Code to handle the specific exception (ZeroDivisionError)
    print(f"Error: {e}")
finally:
    # Code that will be executed whether an exception is raised or not
    print("This block always executes.")
