'''
    Write a Python script to merge two Python dictionaries.
'''

# Create name of d1 and d2 dictionary
d1= {'a': 100, 'b': 200}
d2= {'c': 300, 'd': 400}


# d1 dict copy in merge dict
merge_dict= d1.copy()

# then update d2 dict
merge_dict.update(d2)


# Display result
print("Merge Two Python dictionaries: ",merge_dict)
