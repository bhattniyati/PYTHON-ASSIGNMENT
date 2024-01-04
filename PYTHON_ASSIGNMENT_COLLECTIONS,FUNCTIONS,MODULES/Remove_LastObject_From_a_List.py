'''
    How will you remove last object from a list?
    Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
'''


'''
    Remove the last object from a list in python, you can use the 'pop()'
    method. This method removes and returns the last element from the list.
'''

# list
list1= [2, 33, 222, 14, 25]

remove_element= list1.pop() # Using pop()method

# Print Removed element
print("Removed Element: ", remove_element)

# Print Updated list
print("Updated List: ",list1)

                # 'OR'

'''
    The remove() method removes the first occurrence of the element
    with the specified value
'''

# list
list1= [2, 33, 222, 14, 25]

# Remove element
list1.remove(25)

# Print Result
print("Using Remove Method: ",list1)
        
