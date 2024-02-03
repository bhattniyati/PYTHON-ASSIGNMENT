'''
    Write a Python program to read a file line by line and store it into a list.
'''
# Open File and Read
f= open("Read_File_Line_By_Line.txt","r")

list=[]
# Store in List
list= f.readlines()


# Print List
print(list)