n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if (l[i]%2) !=0:
        x=l[i]
        c+=x
print(c)