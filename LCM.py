n,m=map(int,input().split())
if n>m:
    max=n
else:
    max=m
while True:
    if max%n==0 and max%m==0:
        print(max)
        break
    max=max+1