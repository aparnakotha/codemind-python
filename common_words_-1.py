n=input()
m=input()
n=n.lower()
m=m.lower()
s1=n.split()
s2=m.split()
a=set(s1)
b=set(s2)
print(len(a&b))