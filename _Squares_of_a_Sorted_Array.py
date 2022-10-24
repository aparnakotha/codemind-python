n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    i=i*i
    a.append(i)
a=sorted(a)
print(*a)