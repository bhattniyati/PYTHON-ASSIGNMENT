
print("Swap Two Numbers With Temp Variable...")

A=10
B=20

print()
print("Before Swap Values Are: ","A=",A,"B=",B,)

Temp=A
A=B
B=Temp

print("After Swap Values Are: ","A=",A,"B=",B)

print()

print("Swap Two Numbers Without Temp Variable...")

print()

A=int(input("Enter First Number: "))
B=int(input("Enter Second Number: "))

print("Before Swap Values Are: ","A=",A,"B=",B)

A=A+B
B=A-B
A=A-B

print("After Swap Values Are: ","A=",A,"B=",B)
