'''
    Write a Python program to create and display all combinations of letters,
    selecting each letter from a different key in a dictionary.
    Sample data: {'1': ['a','b'], '2': ['c','d']}
    Expected Output:
    ac ad bc bd
'''

# Sample data
d= {'1':['a','b'], '2':['c','d']}

# Use loop for d['1'] value store in x
for x in d['1']:

    # for d['2'] value store in y
    for y in d['2']:

        # add value of x and y and print result
        print(x+y)
    
