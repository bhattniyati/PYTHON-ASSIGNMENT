'''
    Write a Python program to count the number of lines in a text file.
'''
# Open File And Read
f= open("Max_Length.txt","r")

# Use Readlines and store in d
d= f.readlines()

# Count number of lines 
print("Count The Number Of Lines: ",len(d))