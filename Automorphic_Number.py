n=int(input())
s=n*n
t=str(n)
k=len(t)
i=0
while s!=0:
    r=s%10
    i=i*10+r
    a=str(i)
    b=a[::-1]
    c=len(b)
    if k==c:
        d=int(b)
        if d==n:
            print("Automorphic Number")
            break
    s=s//10
    if k<c:
        print("Not an Automorphic Number")
        break