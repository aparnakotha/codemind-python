n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i!=0:
        a.append(i)
for i in l:
    if i==0:
        a.append(i)
#b.append(a)
for i in a:
    print(i,end=' ')
        