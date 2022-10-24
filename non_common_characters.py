n=input()
m=input()
n=n.lower()
m=m.lower()
n=n.replace(' ','')
m=m.replace(' ','')
c=[]
for i in n:
    if i in c:
        continue
    if i not in m:
        c.append(i)
for j in m:
    if j in c:
        continue
    if j not in n:
        c.append(j)
c=sorted(c)
c=''.join(c)
if len(c)==0:
    print('-1')
else:
    print(c)