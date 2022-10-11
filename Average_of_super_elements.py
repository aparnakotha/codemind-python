n=int(input())
l=list(map(int,input().split()))
d=0
a=[ ]
for i in range(0,n,1):
    if l[i] in a:
        continue
    if l.count(l[i])==l[i]:
        a.append(l[i])
if len(a)==0:
    print('-1')
else:
    z=sum(a)/len(a)
    print('{:.2f}'.format(z))
