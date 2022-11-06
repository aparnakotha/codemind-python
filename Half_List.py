n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
y=len(l)
l=l[::-1]
for i in range(0,(y//2),1):
    a.append(l[i])
for i in range(y//2,y,1):
    b.append(l[i])
b=b[::-1]
for i in a:
    print(i,end=' ')
for i in b:
    print(i,end=' ')