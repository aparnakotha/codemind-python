n=input()
l=len(n)
c=0
for i in range(0,l,1):
    if 90<= ord(n[i]):
        c+=1
print(c)