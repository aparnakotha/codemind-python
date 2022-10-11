n=int(input())
l=list(map(int,input().split()))
c=0
d=0
a=n//2
for i in range(0,a,1):
    
    c+=l[i]
for i in range(a,n,1):
    d+=l[i]
print(c)
print(d)