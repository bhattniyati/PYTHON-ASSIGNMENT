'''
  Write a Python program to count occurrences of a substring in a string.
'''

# Example String:

main_string= "Surat, Ahmedabad, Rajkot, Surat, Amreli, Surat"

# Substring To Count

substring= "Surat" 

occurrences = main_string.count(substring)

# Display the count a substring
print(f"The Substring '{substring}' Appears {occurrences} Times in The Main String...")
