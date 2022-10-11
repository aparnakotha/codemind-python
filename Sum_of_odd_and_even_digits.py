n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(0,n,1):
    if i%2==0:
        c+=l[i]
    else:
        d+=l[i]
if (c-d)==0:
    print("YES")
else:
    print("NO")