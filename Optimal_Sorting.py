t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.copy()
    l=sorted(l)
    if a==l:
        print("0")
    else:
        x=max(l)
        y=min(l)
        print(x-y)
    