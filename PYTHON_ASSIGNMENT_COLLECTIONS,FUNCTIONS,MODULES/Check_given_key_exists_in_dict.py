'''
    Write a Python script to check if a given key already exists in a dictionary.
'''

# Create dict1 
dict1= {'k1': "Python", 'k2': "Java", 'k3': "Php", 'k4': "Javascript"}


# Check key
check_key = 'k3'


# Check if the key exists
if check_key in dict1:
    print(f"The key '{check_key}' exists in the dictionary.")

else:
    print(f"The key '{check_key}' does not exists in the dictionary.")
