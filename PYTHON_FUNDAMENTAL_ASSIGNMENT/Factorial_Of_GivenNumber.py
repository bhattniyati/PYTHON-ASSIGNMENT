'''
    Write a Python program to get the Factorial number of given number.

'''

fact=1

# Enter a number
num=int(input("Enter The Number: "))

for i in range(1,num+1):  # if user enter 5 number so loop will stop at 5 number and every number store in fact var and apply in calculation ex: 1*2*3*4*5
    fact=fact*i     # will perform the fact multiply by i     


# Display the factorial of number
print(fact,"Factorial Of",num)
