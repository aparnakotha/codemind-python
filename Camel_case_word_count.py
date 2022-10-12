n=input()
l=len(n)
x=n.upper()
c=1
for i in range(1,l,1):
    if n[i]==x[i]:
        c+=1
print(c)