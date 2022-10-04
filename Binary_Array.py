n=int(input())
l=list(map(int,input().split()))

x=l.count(0)
y=l.count(1)
if x+y==n:
    print("True")
else:
    print("False")