n=int(input("enter number of terms:"))
a,b=0,1
print("Fibonacci sequence:")
for i in range(n):
    print(a,end="")
    a,b=b,a+b
