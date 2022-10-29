n=int(input())
m=int(input())
x=n+m
y=x
d=0
while x!=0:
    x+=1
    c=0
    for i in range(1,x,1):
        if x%i==0:
            c+=1
    if c==1:
        break
print(x-y)