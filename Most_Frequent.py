n=int(input())
l=list(map(int,input().split()))
m,k=1,0
r=[]
for i in l:
    c=l.count(i)
    m=max(c,m)
for i in l:
    if l.count(i)==m:
        k+=1
        r.append(i)
if k>1:
    print(min(r))
else:
    print(*r)