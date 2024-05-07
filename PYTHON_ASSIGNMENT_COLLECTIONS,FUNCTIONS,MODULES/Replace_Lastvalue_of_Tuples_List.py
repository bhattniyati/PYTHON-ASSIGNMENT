'''
    Write a Python program to replace last value of tuples in a list.
'''

# List of tuples
lists1= [(10,20,30), (40,50,60), (70,80,90)]

update=tuple((lists1[:-1]))

'''
for i in range(len(lists1)):

    lists2= list(lists1[i])
    lists2[-1]= new_value
    lists1[i] = tuple(lists2)
'''


for i in range(len(lists1)):

    i= update + (100,)
    

# Display Result
print("Result:",i)






