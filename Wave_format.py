n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
k=k[::-1]
r=[]
for i in range(0,n):
    if i+1==n:
        break
    if k[i] not in r:
        if k[i+1] not in r:
            r.append(k[i+1])
            r.append(k[i])
if n%2==0:
    print(*r)
else:
    r.append(k[n-1])
    print(*r)