'''
    Write a Python program to find the repeated items of a tuple.
'''

# Create tuple list
tup= (1,3,12,4,3,1,15,12,30,20,20)

# blank list in declare set ... set not allow duplicate values
repeated_items= set()

# Using Loop 
for i in tup:
    if tup.count(i) > 1:

        # store repeated values in i
        repeated_items.add(i)

# Display the result 
print("Repeated Items: ",repeated_items)



