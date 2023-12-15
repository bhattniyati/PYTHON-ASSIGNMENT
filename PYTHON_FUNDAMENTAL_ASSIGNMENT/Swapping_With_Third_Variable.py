
# Swap two numbers with temp variable
print("Swap Two Numbers With Temp Variable...")


# a in 10 nd b in 20 store..
A=10
B=20

print()

# Print a and b before swap
print("Before Swap Values Are: ","A=",A,"B=",B,)


Temp=A  # value of a store in temp variable
A=B # value of b store in a variable
B=Temp # value of temp store in b 

# Print a and b after swap 
print("After Swap Values Are: ","A=",A,"B=",B)  # swap two numbers with temp variable

print()

# Swap two numbers without temp variable
print("Swap Two Numbers Without Temp Variable...")

print()

# Enter two numbers
A=int(input("Enter First Number: "))
B=int(input("Enter Second Number: "))

# Print a and b befor swap 
print("Before Swap Values Are: ","A=",A,"B=",B)

A=A+B 
B=A-B
A=A-B

# Print a and b after swap
print("After Swap Values Are: ","A=",A,"B=",B)
