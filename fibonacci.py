n=int(input("Enter the length of fibonacci series:"))
a=0
b=1
print("The fibonacci series is:")
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
