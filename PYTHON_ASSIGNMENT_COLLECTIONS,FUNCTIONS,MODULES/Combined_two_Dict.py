'''
    Write a Python program to combine two dictionary adding values for common keys.
    d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
'''

# Define 
d1= {'a': 100, 'b': 200, 'c':300}
d2= {'a': 300, 'b': 200, 'd':400}

# d1 item copy in combine_dict
combine_dict= d1.copy()

'''
 Use loop :
            d2 items in key,value then check condition if combine_dict in key so
            combine_dict[key] +equal value
            otherwise combine_dict[key] equal value
'''
for key,value in d2.items():

    if key in combine_dict:

        combine_dict[key] += value

    else:

        combine_dict[key] = value

# Display the result
print(combine_dict)


    
