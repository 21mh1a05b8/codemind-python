n=int(input())
r=[]
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    r.append(a)
for j in range(n):
    b=list(map(int,input().split()))
    l.append(b)
for i in range(n):
    res=[]
    for j in range(n):
        add=r[i][j]+l[i][j]
        res.append(add)
    print(*res)