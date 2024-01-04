'''
    Write a Python program to returns sum of all divisors of a number .
'''

# input a number
num= int(input("Enter a Number : "))

# Create a function
def divisor(number):

    # define a list 
    divisors= [1]

    # use loop range 2 to number
    for i in range(2, number):

        # number % i == 0 so print divisors.append in i 
        if (number % i)==0:
            divisors.append(i)

    # return sum(divisors) 
    return sum(divisors)

# display the result
print(divisor(num))
