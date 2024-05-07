'''

    Write a Python program to check whether an element exists within a tuple.

    '''
# Define tuple:
tuple1= (10,20,30,40,50)

# Element to check
element_check= 20

#check if element_check exists in my_tuple using the in keyword. 
if element_check in tuple1:
    print(f"{element_check} exists in the tuple..")

else:
    print(f"{element_check} does not exists in the tuple..")
