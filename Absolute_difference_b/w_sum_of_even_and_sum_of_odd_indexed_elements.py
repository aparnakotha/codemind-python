n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(0,n,2):
    x=l[i]
    c+=x
for i in range(1,n,2):
    y=l[i]
    d+=y
if c>d:
    print(c-d)
else:
    print(d-c)