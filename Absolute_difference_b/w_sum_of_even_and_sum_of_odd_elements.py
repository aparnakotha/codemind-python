n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(0,n,1):
    if (l[i]%2)==0:
        x=l[i]
        c+=x
    else:
        y=l[i]
        d+=y
if c>d:
    print(c-d)
else:
    print(d-c)