'''
    Write a python program to find the longest words. 
'''
# Open File and Read
f= open("Max_Length.txt","r")

# Store in Variable and read,split 
words= f.read().split()

# Max_len in len of max of words and key= len(the built in len(function)) shorts the 
# strings by length, from shortest to longest..
max_len= len(max(words,key=len))

# Use Loop words in textword and check condition if len of textword equal mex_len and 
# print textword.
for textword in words:
    if len(textword) == max_len:
        print("Longest Word:",textword)

