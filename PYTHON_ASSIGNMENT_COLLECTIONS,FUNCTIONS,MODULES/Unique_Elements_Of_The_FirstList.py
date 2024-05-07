'''
    Write a Python function that takes a list and returns a new list with unique-
    elements of the first list.
'''

# Create a function name of unique_elements

def Unique_elements(input_list):
    return list(set(input_list)) 
                                    
'''
    The set(input_list) creates a set, which automatically removes duplicate elements.
    and list() converts the set back to a list.
'''

# Define original list
original_list= [1,2,2,3,3,3,4,5,6,6,6,6,7,7,8]

# Object of Unique_elements
result= Unique_elements(original_list)

# Print Original list
print("Original List: ",original_list)

# Print Unique elements
print("List with Unique Elements: ",result)
    
