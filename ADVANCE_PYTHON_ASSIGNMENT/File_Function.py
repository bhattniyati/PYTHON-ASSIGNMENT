'''
    What is File function in python? What is keywords to create and writefile. 
'''

'''
File Function: The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode. 
There are various methods (modes) for opening a file:

'x': Create file
'r': Read from file
'w': Write to file
'a': Append to file
'''

#Example:

# Reading from file: 
file= open('Example.txt','r')
text=file.read()
print(text)


# Writing to a file:
file1= open('Example.txt','w')
file1.write("Hello, World !!")

# Append to a file:
file2= open('Example.txt','a')
file2.write('\nAppend More Text...')

