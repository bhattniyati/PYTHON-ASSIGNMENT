'''
    Write a Python script to print a dictionary where the keys are numbers
    between 1 and 15.
'''

# Create blank dictionary named of dict1
dict1= dict()

# Use loop range 1 to 15 and multiply by 2
for x in range(1,15):
    dict1[x] = x**2


# Display the result
print("Dictionary with keys from 1 to 15:")
print(dict1)
