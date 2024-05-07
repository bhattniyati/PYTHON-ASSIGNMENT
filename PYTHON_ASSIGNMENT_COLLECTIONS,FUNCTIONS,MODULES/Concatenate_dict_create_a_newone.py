'''
    Write a Python script to concatenate following dictionaries to create a
    new one.
'''


# Create three dictionaries 'dic1', 'dic2', and 'dic3' with key-value pairs
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}


# Create an empty dictionary 'dict4'
dict4= {}   


# Using a loop
for d in (dict1,dict2,dict3):

    # Update 'dict4' adding the key-value pairs from the current dictionary 'd'
    dict4.update(d)


# Display result
print("New one dictionary: ",dict4)
