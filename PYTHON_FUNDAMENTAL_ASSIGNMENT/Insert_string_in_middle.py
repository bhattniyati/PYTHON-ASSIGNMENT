'''
    Write a Python function to insert a string in the middle of a string.
'''

# Create a function 
def insert_string(original,insert):

    result_string= original[:5] + insert + original[5:]
    return result_string


# input a string
original_string= "Hello , World !!"
inserted_string= "Python"

# object of insert_string 
result= insert_string(original_string,inserted_string)

# print original string
print("Original String: ",original_string)

# print inserted string
print("Inserted String: ",inserted_string)

# print result string
print("Result String: ",result)
