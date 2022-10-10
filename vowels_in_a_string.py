n=input()
a=input()
l=len(n)
for i in range(0,l,1):
    if n[i]==a:
        print("True")
        print(i)
        break
else:
    print("False")