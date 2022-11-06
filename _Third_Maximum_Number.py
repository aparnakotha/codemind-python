n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=sorted(l)
if len(l)>=3:
    print(l[-3])
else:
    print(max(l))


