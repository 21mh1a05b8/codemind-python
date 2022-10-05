n,k=map(int,input().split())
l=list(map(int,input().split()))
r=[]
k=k-1
for i in range(0,len(l)):
    if i>k:
        r.append(l[i])
for i in range(0,len(l)):
    if i<=k:
        r.append(l[i])
print(*r)