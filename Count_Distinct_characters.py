n=input()
n=list(set(n.lower()))
n=sorted(n)
c=0
for i in n:
    if i!=" " :
        c+=1
print(c)