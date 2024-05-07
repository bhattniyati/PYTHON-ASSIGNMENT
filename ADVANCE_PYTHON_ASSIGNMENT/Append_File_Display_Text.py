'''
    Write a Python program to append text to a file and display the text.
'''

# Open File and append
f= open("Append_file.txt","a")

# Enter Data
enter= input("Enter Data: ")

# Write File
f.write("\n"+enter)

# Second Time Open File and Read File
f= open("Append_file.txt","r")

# Print in Read File
print(f.read())

# close file
f.close()