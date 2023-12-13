'''
    Write a Python program to test whether a passed letter is a vowel or not.

'''

vowel=['a','e','i','o','u'] # store the vowel


# Enter a alphabet
letter=str(input("Enter Any Alphabet: "))

'''
    Chcek the condition if user enter a letter is in store vowel so print the msg letter is vowel,
    but user enter a letter is not in store vowel so print the msg letter is not a vowel

'''

if letter in vowel:
    print("The Letter is a Vowel..")

else:
    print("The Letter is not a Vowel..")
