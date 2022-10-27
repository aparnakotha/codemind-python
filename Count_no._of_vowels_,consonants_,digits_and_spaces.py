n=input()
s='a,e,i,o,u,A,E,I,O,U'
a=0
b=0
c=0
for i in n:
    if i in s:
        a+=1
    if i==' ':
        b+=1
    if i.isdigit()==True:
        c+=1
x=len(n)
y=x-(a+b+c)
print("Vowels:",a)
print("Consonants:",y)
print("Digits:",c)
print("White spaces:",b)