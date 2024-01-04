'''
    Write a Python program to generate and print a list of first and last 5-
    elements where the values are square of numbers between 1 and 30.
'''


# Define a empty list
square_list= []


# Using loop through generate squares of numbers between 1 and 30
for number in range(1,30):

    square_list.append(number**2) # Calculate the square of 'number' and append to the list 'square_list' 

# Extract The First and Last 5 Elements
First_5_elements = square_list[:5]
Last_5_elements = square_list[-5:]

# Print the results
print("First 5 elements:", First_5_elements)
print("Last 5 elements:", Last_5_elements)

