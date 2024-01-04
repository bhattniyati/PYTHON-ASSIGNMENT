'''
    How can you pick a random item from a list or tuple?
'''


'''
    Use the random.choice() method: This method returns randomly selected element from the 
                                    specified sequence..

'''

import random

# Create a list
lists= [10,20,30,40,50]

result= random.choice(lists)


# Display result
print(result)
