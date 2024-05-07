'''
    Write a Python program to unzip a list of tuples into individual lists.
'''

# Define list of tuple
list_of_tuple= [(1,'a',10), (2,'b',20), (3,'c',30), (4,'d',40)]


# zip(*list_of_tuple) is used to unzip the list of tuples.
individual_lists= list(zip(*list_of_tuple))


print("List Of Tuple: ",list_of_tuple)  
print("Individual Lists: ",individual_lists)
