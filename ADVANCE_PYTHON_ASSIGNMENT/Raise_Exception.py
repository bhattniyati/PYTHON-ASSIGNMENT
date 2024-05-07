'''
    Write python program that user to enter only odd numbers, else will
    raise an exception.
'''


try:
    # Code that may raise an exception
    user_input=int(input("Enter an odd number: "))
    

    # use condition if number % 2 == 1 so print odd number otherwise raise valuerror in else part
    # and print an error..
    if user_input % 2==1:
        print(f"You enterd an odd number: {user_input}")
            
    else:
        raise ValueError("Please enter only odd number..")

except ValueError as e:
    # Code to handle the specific exception (ValueError)
    print(f"Error: {e}")
