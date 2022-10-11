n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n,1):
    if l[i]%2 ==0:
        break
    else:
        c+=l[i]
print(c)