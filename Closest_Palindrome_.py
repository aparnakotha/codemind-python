n=int(input())
t=n
k=n
while n>0:
    t+=1
    p=t
    rem=0
    while p!=0:
        r=p%10
        p=p//10
        rem=rem*10+r
    if(t==rem):
        m=t
        break
while n>0:
    k-=1
    w=k
    rem1=0
    while w!=0:
        r=w%10
        w=w//10
        rem1=rem1*10+r
    if(k==rem1):
        mi=k
        break
a=m-n
b=n-mi
if a>b:
    print(mi)
elif a==b:
    print(mi,m,end=' ')
else:
    print(m)