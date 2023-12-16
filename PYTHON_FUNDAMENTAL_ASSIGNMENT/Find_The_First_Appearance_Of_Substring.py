'''
    Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
    if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''

# Input a string..
string= "The Weather is Not Poor Today..."


index_Not= string.find('Not')
index_Poor= string.find('Poor')

'''
    if index_poor > index_not so print result in substrung with good..and condition false so print result in string 

if index_Poor > index_Not:
    result= string[:index_Not]+ 'Good' + string[index_Poor+4:]
else:
    result=string

# Display result...
print("Result: ",result)
