n=int(input())
l=list(map(int,input().split()))
c=0
s=set(l)
for i in s:
    c+=l.count(i)//2
print(c)