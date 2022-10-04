n=input()
m=input()
n=n.lower()
m=m.lower()
r=[]
for i in n:
    for j in m:
        if i==j and i!=" ":
            if i not in r:
                r.append(i)
print(len(r))