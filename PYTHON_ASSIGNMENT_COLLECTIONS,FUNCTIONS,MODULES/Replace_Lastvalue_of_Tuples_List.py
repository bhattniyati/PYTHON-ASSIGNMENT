'''
    Write a Python program to replace last value of tuples in a list.
'''

# List of tuples
lists1= [(10,20,30), (40,50,60), (70,80,90)]


# Use list Comprehension: is used to iterate through each tuple t in lists1 
lists2= [(t[:-1] + (100,)) for t in lists1]


# Display Result
print("Original List of Tuples: ",lists1)
print("Result: ",lists2)





