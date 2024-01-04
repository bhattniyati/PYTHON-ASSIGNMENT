'''
    Write a Python function that takes two lists and returns true if they have-
    at least one common member.
'''

# Define a function called common_member
def Common_member(list1,list2):

    result= False

    # Iterate through each element 'x' in 'list1'
    for x in list1:

        # Iterate through each element 'y' in 'list2'
        for y in list2:

            # Check a condition if elements a and y are equal
            if x==y:
                result=True
                
    return result


# Define a lista and listb  
lista=[1,2,3,4,5]
listb=[5,6,7,8,9,10]

# Object of common member
result= Common_member(lista,listb)

# print result
print(result)
