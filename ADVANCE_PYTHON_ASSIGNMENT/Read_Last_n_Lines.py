'''
    Write a Python program to read last n lines of a file. 
'''

# Open file and Read
f= open("Read_First_Line.txt","r")

# Use readlines , index and Last line read
print(f.readlines()[-1])