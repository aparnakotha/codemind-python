n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n,2):
    x=l[i]
    c+=x
print(c)