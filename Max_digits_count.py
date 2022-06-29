n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    i=str(i)
    k=len(i)
    r.append(k)
a=max(r)
c=0
for i in r:
    if i==k:
        c+=1
print(c)