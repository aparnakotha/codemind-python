n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n,1):
    x=(l[i])
    s=str(x)
    y=len(s)
    if y%2==0:
        c+=1
print(c)