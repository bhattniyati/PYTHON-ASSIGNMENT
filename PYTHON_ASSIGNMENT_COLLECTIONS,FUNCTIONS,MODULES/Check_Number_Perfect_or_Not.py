'''
    Write a Python function to check whether a number is perfect or not.
'''

# input a number 
n= int(input("Enter a Number: "))


# create a function named perfect_num 
def perfect_num(n):

    # declare sum
    sum=0

    # Use loop 1 to n 
    for x in range(1,n):

        # condition 
        if n%x == 0:
            sum += x


    return sum==n


# print the result call function 
print(perfect_num(n))
