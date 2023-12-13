'''
  Write a Python program to get a single string from two given strings,
  separated by a space and swap the first two characters of each string.

'''
# Two Given Strings:

string1= "English"
string2= "Gujarati"

'''
  new_string = Guglish+ ' '+ Enjarati= Guglish Enjarati -- string2[:2] is store string2 of first two letter and 
                                                           string1[2:] is store string1  of 2 index with last all letter

'''

new_string= string2[:2]+ string1[2:]+ ' ' + string1[:2]+string2[2:] 

# Display the original strings
print(f"Original Strings: \nString 1: {string1} \nString 2: {string2}")

print("\nAfter Separated by Space & Swapping First Two Character: ")

# Display new string
print(new_string)



