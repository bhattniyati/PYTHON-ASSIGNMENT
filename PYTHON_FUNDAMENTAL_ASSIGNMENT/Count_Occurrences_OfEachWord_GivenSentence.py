'''
    Write a Python program to count the occurrences of each word in a
    given sentence.
'''

# Enter A String
string= input("Enter A String: ")

string=string.split()  # Split The String


i=0

'''
    Use of while loop and for loop
    for x in string 
    and chcek the condition if string of i == x 
    so count count and add 1
    and print string of i..
'''

while i<len(string):
    count=0
    for x in string:
        if string[i]==x:
            count=count+1
    print(string[i],"Present", count,"Times")

    i=i+1
