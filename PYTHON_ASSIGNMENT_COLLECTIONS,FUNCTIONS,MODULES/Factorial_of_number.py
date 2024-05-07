'''
    Write a Python function to calculate the factorial of a number (a nonnegative integer)
'''


# Create a function named fact_num
def fact_num(n):

    # condition check if the number is 0
    if n==0:

        # number is 0 , return 1 
        return 1

    else:

        # number is not 0 , call the function with (n-1) and multiply with number 
        return n*fact_num(n-1)


# input a number 
n= int(input("Enter a Number: "))

# display the result
print(fact_num(n))
        
