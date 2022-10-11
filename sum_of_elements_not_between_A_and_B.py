n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
d=0
for i in (l):
    if i>=x and i<=y :
        pass
    else:
        c+=1
        d+=i

print(d)

