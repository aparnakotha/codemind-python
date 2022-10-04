n=int(input())
l=list(map(int,input().split()))
c=0
d=len(l)

for i in range(0,n,1):
    if l[i]%2 == 0:
        c+=1
if c==d:
    print("True")
else:
    print("False")