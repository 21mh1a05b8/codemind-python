n=input()
m=input()
n=n.lower()
m=m.lower()
n=n.split()
m=m.split()
c=0
for i in n:
    for j in m:
        if n.count(i)==1 and m.count(j)==1:
            if i==j:
                c+=1
print(c)