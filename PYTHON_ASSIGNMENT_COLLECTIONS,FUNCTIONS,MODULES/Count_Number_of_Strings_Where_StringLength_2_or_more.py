'''
    Write a Python program to count the number of strings where the string
    length is 2 or more and the first and last character are same from a given
    list of strings.
'''

# Create a string list
string_list=['aba', 'xyz', 'sis', 'local','mam', 'abc']

count= 0

# Using loop String_list in s 
for s in string_list:

    # condition check if len of s >=2 and s of 0 index and s of last index equal so count += 1 
    if len(s) >=2 and s[0] == s[-1]:

        count += 1


# Display Result
print(f"Number of strings with length 2 or more and same first and last character: {count}")
