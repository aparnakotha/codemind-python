n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
d=0
a=[]
for i in (l):
    if i>=x and i<=y :
        a.append(i)
        d+=i
        c+=1
if c==0:
    print('-1')
else:
    print(d)