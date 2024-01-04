'''
    Write a Python program to find the highest 3 values in a dictionary.
'''


# Create dictionary
dict1= {'a': 300, 'b': 400, 'c': 100, 'd': 500, 'e': 200}


# Using sorted this sorts the values in descending order and [:3] takes the first 3 values..
highest_value= sorted(dict1.values(), reverse= True)[:3]


# Display the result

print("Dictionary: ", dict1)
print("Highest 3 values: ",highest_value)
