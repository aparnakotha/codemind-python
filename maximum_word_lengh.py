n=input()
s=n.split()
l=len(s)
max=len(s[0])
for i in range(1,l,1):
    if len(s[i]) > max:
        max=len(s[i])
print(max)