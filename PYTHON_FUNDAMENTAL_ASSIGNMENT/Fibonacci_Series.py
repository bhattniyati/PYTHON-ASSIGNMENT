'''
    Write a Python program to get the Fibonacci series of given range.
'''

# declare 3 variable with value
n1=0
n2=1
n3=2
n3=n1+n2 # n3 store sum of n1, n2

# Enter a steps
end=int(input("Enter How Many Steps You Want? "))

# print n1,n2,n3 and end= "" blank
print("Fibonacci Series: ",n1,n2,n3,end=" ")

'''
    loop starting from 1 and end-2 in every number is '-' by 2
    and print n3
'''

for i in range(1,end-2):
    n1=n2
    n2=n3
    n3=n1+n2
    print(n3)
