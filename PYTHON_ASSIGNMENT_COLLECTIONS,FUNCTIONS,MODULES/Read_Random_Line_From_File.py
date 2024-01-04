'''
    Write a Python program to read a random line from a file.
'''

import random 

# open file
f= open("my_file1.txt", "r")

# read a line and split line using splitliness-- this split a multi-line string into a list of lines..
lines= f.read().splitlines()
print(random.choice(lines))

# display the result
print("my_file1.txt")
