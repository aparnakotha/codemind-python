n,m=map(int,input().split())
if n>1 and m>1:
    for i in range(n+1,0,-1):
        if n%i==0 and m%i==0:
            print(i)
            break