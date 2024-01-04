'''
    Write a Python program to remove an empty tuple(s) from a list of tuples.
'''

# Define List of tuple
list_of_tuple= [(1,2,3), (), (4,5,6), (), (7,8,9), (10,20)]

# Use loop 
for x in list_of_tuple:

    # condition check len of x equal 0 so used remove method and print empty tuples..
    if len(x) == 0:
        list_of_tuple.remove(x)

# Display the result
print("Remove Empty Tuple From List",list_of_tuple)
        