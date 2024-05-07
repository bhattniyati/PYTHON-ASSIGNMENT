'''
    Write a Python program to reverse a tuple.
'''

# Define Tuple
t1= ("Python", 10,20,30,"Java")


#the[::-1] slice notation is used to reverse the order of elements in the tuple. 
reversed_tuple = t1[::-1]


# Display Result
print("Original Tuple: ",t1)
print("Reversed Tuple: ",reversed_tuple)
