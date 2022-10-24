n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(n):
    m=l[i]+k
    c=0
    for j in range(n):
        if m>=l[j]:
            c+=1
    if c==n:
        print("True",end=' ')
    else:
        print("False",end=' ')