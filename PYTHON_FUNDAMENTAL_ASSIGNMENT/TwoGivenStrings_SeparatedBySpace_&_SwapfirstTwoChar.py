
# Two Given Strings:

string1= "English"
string2= "Gujarati"

new_string= string2[:2]+ string1[2:]+ ' ' + string1[:2]+string2[2:]


print(f"Original Strings: \nString 1: {string1} \nString 2: {string2}")
print("\nAfter Separated by Space & Swapping First Two Character: ")
print(new_string)



