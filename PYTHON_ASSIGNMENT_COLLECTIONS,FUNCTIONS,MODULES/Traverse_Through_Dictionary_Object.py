'''
    How Do You Traverse Through A Dictionary Object In Python?
'''

# Create a Dictionary
data= {

    "Name": "Ruchi",
    "subject": "Python",
    "Marks": 50
    }


# Use loop data store in key value 
for key,value in data.items():

    # Print key value
    print(f"{key}={value}")
