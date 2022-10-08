n=input()
n=n.lower()
r=[]
for i in n:
    if n.count(i)==1:
        if i!=" ":
            r.append(i)
print(len(r))