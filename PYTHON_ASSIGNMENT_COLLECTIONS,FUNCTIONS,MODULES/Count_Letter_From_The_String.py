'''
    Write a Python program to create a dictionary from a string.
    Note: Track the count of the letters from the string.
    Sample string: 'w3resource'
    Expected output:
    {'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''

# Create a sample string
sample_string= 'w3resource'

# Craete a empty dictionary to store letters count..
count_letter= {}



# Using loop simple_string in letter
for letter in sample_string:
    
    count_letter[letter]= count_letter.get(letter, 0) + 1


# Display The Result
print(count_letter)



    
