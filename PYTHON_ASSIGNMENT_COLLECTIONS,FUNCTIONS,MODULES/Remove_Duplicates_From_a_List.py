'''
    Write a Python program to remove duplicates from a list.
'''

'''
    Using set function.. set cannot allow duplicates value
'''

# Define list
original_list= [10,20,30,45,20,45,10,100]

unique_list= list(set(original_list))  


# print original list
print("Original List: ",original_list)

# print after removing duplicates list
print("List After Removing Duplicates : ",unique_list)
