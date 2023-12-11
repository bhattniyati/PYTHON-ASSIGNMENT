'''
    Write a Python program to count the occurrences of each word in a
    given sentence.
'''

# Enter A String
string= input("Enter A String: ")

string=string.split()  # Split The String


i=0


while i<len(string):
    count=0
    for x in string:
        if string[i]==x:
            count=count+1
    print(string[i],"Present", count,"Times")

    i=i+1
