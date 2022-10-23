n=input()
m=input()
n=n.lower()
m=m.lower()
s1=n.split()
s2=m.split()
for i in s2:
    if i in s1:
        print(i,end=' ')
