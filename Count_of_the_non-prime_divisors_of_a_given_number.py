n=int(input())
d=0
for i in range(1,n+1,1):
    if n%i==0:
        c=0
        for k in range(1,i+1,1):
            if i%k==0:
                c+=1
        if c>2 or c==1:
            d+=1
print(d)