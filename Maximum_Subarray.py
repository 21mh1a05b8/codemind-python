n=int(input())
l=list(map(int,input().split()))
m=-10
s=0
for i in range(n):
    s=0
    for j in range(i,n):
        s+=l[j]
        m=max(s,m)
print(m)