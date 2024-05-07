'''
    Write a Python function to check whether a number is in a given range.
'''

# Define function named check_num
def check_num(n):

    # Check condition n between 1 to 10 , if condition true so print number is given the range
    # else condition false so print not given range
    if n in range(1,10):
        print(f"{n} is in the given range")

    else:
        print(f"{n} is outside the given range")


# Display the result
check_num(5)
check_num(11)
