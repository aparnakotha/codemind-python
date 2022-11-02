n=int(input())
while n>9:
    rem=0
    while n!=0:
        r=n%10
        n=n//10
        rem+=r
    n=rem
print(n)