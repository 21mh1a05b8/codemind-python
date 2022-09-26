n,m=map(int,input().split())
r=[]
for i in range(n):
    l=list(map(int,input().split()))
    s=0
    for i in l:
        s+=i
    r.append(s)
print(max(r))