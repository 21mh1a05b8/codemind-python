n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(0,n-1):
    l.pop(0)
    m=max(l)
    r.append(m)
r.append("-1")
print(*r)