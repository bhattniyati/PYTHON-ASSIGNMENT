'''
    Write a Python program to select an item randomly from a list.
'''


import random

# Define a list
lists= ["Ahmedabad","Surat","Amreli","Rajkot","Vadodara","Gandhinagar"]


# The random.choice(lists) function is used to randomly select an item from the list..
random_item= random.choice(lists)

# Print original list
print("Original List: ",lists)

# Print randomly selected item
print("Randomaly Selected Item: ",random_item)
