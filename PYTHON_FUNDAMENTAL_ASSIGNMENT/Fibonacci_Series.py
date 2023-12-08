


n1=0
n2=1
n3=2
n3=n1+n2

end=int(input("Enter How Many Steps You Want? "))

print("Fibonacci Series: ",n1,n2,n3,end=" ")

for i in range(1,end-2):
    n1=n2
    n2=n3
    n3=n1+n2
    print(n3)
