n=int(input())
l=list(map(int,input().split()))
a=[ ]
for i in range(0,n,1):
    if l[i] in a:
        continue
    a.append(l[i])
for i in a:
    print(i,end=' ')