'''
    Write a Python program to count the frequency of words in a file.
'''
# import counter and count words
from collections import Counter

# open file and read file
f= open("Frequency_Words.txt","r")

# read and count words store in words 
words= Counter(f.read().split())

# print count frequency of words 
print("Count Frequency Of Words: ",words)
