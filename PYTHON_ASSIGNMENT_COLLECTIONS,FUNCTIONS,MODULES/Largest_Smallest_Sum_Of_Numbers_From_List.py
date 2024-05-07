'''
    Write a Python function to get the largest number, smallest num and sum-
    of all from a list.
'''

# Create a function name of numbers
def Numbers(number_list):

    Largest_number= max(number_list) # Using max() function
    Smallest_number= min(number_list) # Using min() function
    Sum_of_all_numbers= sum(number_list) # Using sum() function

    return Largest_number,Smallest_number,Sum_of_all_numbers


# Numbers List
lists= [10,5,20,4,30,2]

# Object of Numbers
n1= Numbers(lists)

# print largest number
print("Largest Number: ",n1[0])

# print smallest number
print("Smallest Number: ",n1[1])

# print sum of numbers
print("Sum of all Numbers: ",n1[2])

# print all
print("\nLargest,Smallest,Sum_of_all_numbers:",n1)

    
