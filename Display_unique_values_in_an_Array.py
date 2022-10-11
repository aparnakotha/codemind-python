n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in range(0,n,1):
    if l[i] in a:
        continue
    if l.count(l[i])==1:
        a.append(l[i])
        c+=1
if c==0:
    print('-1')
else:
    print(*a)