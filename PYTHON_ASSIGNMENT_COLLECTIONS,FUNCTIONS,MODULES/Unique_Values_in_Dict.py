'''
    Write a Python program to print all unique values in a dictionary.
'''

dict1= {'a': 100, 'b': 200, 'c': 300, 'd': 200, 'e': 100}


unique_values= set()


for value in dict1.values():
    unique_values.add(value)



print("Original Dictionary: ",dict1)
print("Unique Values: ",unique_values)
