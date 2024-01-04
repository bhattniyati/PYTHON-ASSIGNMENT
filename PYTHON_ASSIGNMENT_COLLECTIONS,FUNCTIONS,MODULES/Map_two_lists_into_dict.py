'''
    Write a Python program to map two lists into a dictionary.
'''

# Create two lists
keys= ['key1', 'key2', 'key3']
values= ['value1', 'value2', 'value3']

# Using zip function two lists into a dictionary    
map_dict= dict(zip(keys, values))


# Display result
print("Original Lists: ")
print("Keys:",keys)
print("Values:",values)
print("\nMap two lists into a dictionary:", map_dict)
