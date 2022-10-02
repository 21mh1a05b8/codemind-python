n=input()
n=n.split()
m=[]
mi=[]
s,s1=0,0
for i in n:
    k=ord(max(i))
    x=ord(min(i))
    print((abs(x-k)),end=" ")