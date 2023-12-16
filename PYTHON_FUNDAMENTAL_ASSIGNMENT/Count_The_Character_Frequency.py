'''
    Write a Python program to count the number of characters (character frequency) in a string.
'''

count=0

# Enter A String
string = input("Enter The String: ")
character=[]

'''
    for char in string
        if character == character so count a number and add +=1 and print count number
'''

for char in string:
    if character==character:
        count+= 1

    print("count",count)  # Count The Character

# Print Number Of Character
print("The Number Of Character is: ",count)
