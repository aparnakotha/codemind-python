n=int(input())
l=list(map(int,input().split()))
for i in range(0,n,1):
    if l[i]%2 != 0:
        print(l[i],end=' ')
for i in range(0,n,1):
    if l[i]%2 == 0:
        
        print(l[i],end=' ')