'''
    How Do You Check The Presence Of A Key In A Dictionary?
'''
# Create a dict
my_dict= {'a': 1, 'b': 2, 'c': 3}

# Define a key
check_key= 'b'

# Condition Check if key in my_dict so print key is present else not present using 'in' operator.
if check_key in my_dict:

    print(f"The key '{check_key}' is present in the dictionary.")

else:

    print(f"The key '{check_key}' is not present in the dictionary.")
    
