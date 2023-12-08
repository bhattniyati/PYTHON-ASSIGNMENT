

string= input("Enter a String: ")

if len(string) > 3:
    if string.endswith('ing'):
        result= string + 'ly'

    else:
        result= string + 'ing'

else:
    result= string


print("Result: ",result)
