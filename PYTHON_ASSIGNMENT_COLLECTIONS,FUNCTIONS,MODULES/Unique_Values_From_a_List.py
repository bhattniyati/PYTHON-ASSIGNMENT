'''
    Write a Python program to get unique values from a list.
'''

# Define List:
list1= [1,2,3,4,4,5,5,5,6,7,8,8,9]


# Using set: which automatically removes duplicates values. and list() converts the set back to a list.
unique_values= list(set(list1))


# Display Original List
print("Original List: ",list1)

# Display Result
print("Unique Values: ",unique_values)
