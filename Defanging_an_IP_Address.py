n=input()
n=list(n)
for i in range(len(n)):
    if n[i]=='.' :
        n[i]='[.]'

print(''.join(n))