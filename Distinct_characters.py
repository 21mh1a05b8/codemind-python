s=input()
s=s.lower()
s=list(s)
c=[]
for i in s:
    if(s.count(i)==1 and i!=' '):
        c.append(i)
c=sorted(c)
for i in c:
    print(i,end="")