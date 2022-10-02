n=input()
l=len(n)
for i in range(l):
    c=n.count(n[i])
    if c==1:
        print(i)
        break
    i+=1
else:
    print("-1")