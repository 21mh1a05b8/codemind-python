n=input()
v="aeiouAEIOU"
n=n.split()
r=[]
c=0
for i in n:
    m=[]
    for j in i:
        if j in v:
            m.append(j)
    r.append(len(m))
k=min(r)
c=0
for i in r:
    if i==k:
        c+=1
print(c)