n=input()
n=n.lower()
v="aeiou"
n=n.split()
r=[]
for i in n:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
print(min(r))