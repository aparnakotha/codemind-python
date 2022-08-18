n=int(input())
a=0
b=1
if(n==a or n==b):
    print("True")
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    if (n==c):
        print("True")
        break
else:
    print("False")