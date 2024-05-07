'''
    Write a Python program to read first n lines of a file.
'''

# Open File and Read
f= open("Read_First_Line.txt","r")

# Use redalines, index and First lines read
print(f.readlines()[0])