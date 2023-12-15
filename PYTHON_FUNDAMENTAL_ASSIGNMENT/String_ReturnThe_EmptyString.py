'''
    Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
    If the string length is less than 2, return instead of the empty string.
'''

# Enter a string
string= input("Enter A String: ")

'''
    Condition:
        if string is less than true so print empty string
        else 
            string is > 2 so print string of add first two letter and add last two letter
'''

if len(string) < 2:
    result= " "

else:
    result= string[:2] + string[-2:]


# Print result
print("Result String: ",result)




