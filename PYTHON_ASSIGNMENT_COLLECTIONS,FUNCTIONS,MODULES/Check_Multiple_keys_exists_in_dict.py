'''
    Write a Python program to check multiple keys exists in a dictionary.
'''


# Create a dictionary named dict1
dict1= {

    'roll_no': 70,
    'name': 'Rishi',
    'subject': 'English',
    'class': 'V'
    }

# keys into set 
keys= set({'roll_no', 'name', 'subject'})

# Check keys in a dict1 using issubset method..
# Thid method returns true if all keys in dict1 otherwise returns false..
res= keys.issubset(dict1.keys())

# Display the result
print(res)

