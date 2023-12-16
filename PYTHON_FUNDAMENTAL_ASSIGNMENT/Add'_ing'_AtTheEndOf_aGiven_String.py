'''
    Write a Python program to add 'ing' at the end of a given string (lengthshould be at least 3).
    If the given string already ends with 'ing' then add 'ly' instead
    if the string length of the given string is less than 3, leave it unchanged.
'''

# Enter String
string= input("Enter a String: ")


'''
    Condition if string grater than 3 so second time check a condition if the string ends with ing so print result string + ly,
    and condition false so print result string + ing as it is ,
    and outer condition false so print result only string...
'''

if len(string) > 3:
    if string.endswith('ing'):   
        result= string + 'ly'

    else:
        result= string + 'ing'

else:
    result= string

# Print The Result
print("Result: ",result)
