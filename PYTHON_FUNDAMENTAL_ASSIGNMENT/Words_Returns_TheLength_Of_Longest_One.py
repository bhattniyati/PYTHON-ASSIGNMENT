'''
    Write a Python function that takes a list of words and returns the length -
    of the longest one.
'''

# Create a word name of function
def word(my_list):

    count=0
    
    '''
        Use for loop and in check the condition len(item) is grater than equal count so count the len(item)
    '''
    
    for item in my_list:

        if len(item) >= count:
            count= len(item)

    return count



# input a lists
lists= ["Ahmedabad", "Surat", "Gandhinagar", "Amreli", "Rajkot"]

# Object of word
w1= word(lists)

# Print longest word
print("Longest word count is: ",w1)
