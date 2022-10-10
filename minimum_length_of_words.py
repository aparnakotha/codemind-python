n=input()
s=n.split()
l=len(s)
min=len(s[0])
for i in range(1,l,1):
    if len(s[i]) < min:
        min=len(s[i])
print(min)