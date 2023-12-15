'''
    Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''

# Enter Three Numbers
num1= int(input("Enter The First Number: "))
num2= int(input("Enter The Second Number: "))
num3= int(input("Enter The Third Number: "))

'''
    Condition:
        if num1 and num2 are equal or num2 and num3 are equal or num1 and num3 are equal any condition is true so print 0
        else 
               given 3 numbers are different so sum of three numbers
'''

if num1==num2 or num2==num3 or num1==num3:
    result_sum=0

else:
    result_sum= num1+num2+num3

# Print result
print("The Sum is: ",result_sum)
