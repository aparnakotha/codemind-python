n=input()
l=len(n)
if n.count('0')>1 or n.count('1')>1 or n.count('2')>1 or n.count('3')>1 or n.count('4')>1 or n.count('5')>1 or n.count('6')>1 or  n.count('7')>1 or n.count('8')>1 or n.count('9')>1:
    print("Not Unique Number")
    i+=1
else:
    print("Unique Number")