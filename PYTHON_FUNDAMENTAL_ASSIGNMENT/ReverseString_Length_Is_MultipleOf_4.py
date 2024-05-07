'''
    Write a Python function to reverses a string if its length is a multiple of 4.
'''

# Create a Reverse_string name of function

def reverse_string(input_string):

    '''
          condition given string is multiple of 4 so print reverse string and condition false
          so print given string as it is
    '''

    if len(input_string) % 4 == 0: 

        return input_string[::-1] # Reversing the string using slicing

    else:

        return input_string


# Input string
input_str1= "ABCD"
input_str2= "SURAT"

# object of reverse_string
result= reverse_string(input_str1)

# print original string
print("Original String: ",input_str1)

# print result string
print("Result String: ",result)

    
