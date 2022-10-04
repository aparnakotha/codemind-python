n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(0,n,1):
    x=l[i]
    c+=x
y=c//n
for i in range(0,n,1):
    if l[i] <= y:
        d+=1
print(d)