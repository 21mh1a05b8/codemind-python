n=int(input())
l=list(map(int,input().split()))
r=[]
m=[]
for i in l:
    k=l.count(i)
    if i not in r:
        r.append(i)
        m.append(i)
        m.append(k)
print(*m)