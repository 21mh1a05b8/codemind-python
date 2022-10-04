n=input()
r=[]
for i in n:
    r.append(n.count(i))
r=set(r)
r=sorted(list(r))
r=r[::-1]
if len(r)>1:
    k=r[1]
else:
    print("-1")
c=0
for i in n:
    if n.count(i)==k:
        print(i)
        c+=1
        break
if c==0:
    print("-1")