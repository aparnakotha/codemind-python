t=int(input())
for i in range(t):
    a=int(input())
    n=input()
    for i in range(0,a,1):
        x=n.count(n[i])
        if x==1:
            print(n[i])
            break
    else:
        print('-1')