'''
Write a Python program to copy the contents of a file to another file. 
'''
# Open File1 
file= open("File1.txt","r") 

# Open File2 and Write
f= open("File2.txt","w")

# Use loop for copy one file to another file: line in store File 1 and another file in write file
for line in file:
    f.write(line)