'''
    Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''


# Enter Two Numbers: 
num1= int(input("Enter the First Number: "))
num2= int(input("Enter The Second Number: "))


# Condition num1 nd num2 equal nd difference is 5 so condition true else condition is false...
if num1==num2 or num1+num2==5 or  num1-num2==5:
    result= True

else:
    result=False


# Display Result
print(result)
