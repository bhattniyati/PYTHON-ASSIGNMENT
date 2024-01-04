'''
    Write a Python function that checks whether a passed string is palindrome or not
'''

# Create a function named ispalindrome 
def ispalindrome(string):

    # Return reverse string and string equal so string is palindrome
    return string == string[::-1]


# define string
string= "dad"

# display the result
result= ispalindrome(string)


# Check condition
if result:
    print("True")

else:
    print("False")


    
