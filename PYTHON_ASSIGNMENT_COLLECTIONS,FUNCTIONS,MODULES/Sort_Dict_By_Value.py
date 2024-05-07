'''
    Write a Python script to sort (ascending and descending) a dictionary by value.
'''

# Create dictionary
data= {'John': 40, 'Sid': 30, 'Isha': 26, 'Elisa': 60}


# Sort the dictionary by value in ascending order
# Use lambda function
sort_ascending= dict(sorted(data.items(), key= lambda x: x[1]))

# Sort the dictionary by value in descending order
# The reverse=True sorts the list in descending order by value.
sort_descending= dict(sorted(data.items(), key= lambda x: x[1], reverse=True))

# Display the result
print("Original Dictionary: ", data)
print("Sorted Dictionary (Ascending):", sort_ascending)
print("Sorted Dictionary (Descending):", sort_descending)
