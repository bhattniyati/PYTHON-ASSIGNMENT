'''
    Write a Python program to combine values in python list of dictionaries.
    Sample data: 
    Expected Output:
    Counter ({'item1': 1150, 'item2': 300})

'''

# Import Counter
from collections import Counter


# Create a List of Dictionaries
lists= [{'item': 'item1','amount': 400},{'item': 'item2','amount':300},{'item': 'item1','amount': 750}]
print(lists)

print()

data= Counter()


# Use Loop lists in i
for i in lists:

    # i['item'] + and = i['amount']
    data[i['item']] += i['amount']
    print(i)

print()

# Display Result
print("Combine Value in List Of Dictionaries: ",data)
