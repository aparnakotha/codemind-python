n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0, n, 1):
    x=l[i]
    c+=x
y=c/n
y1="{:.2f}".format(y)
print(y1)