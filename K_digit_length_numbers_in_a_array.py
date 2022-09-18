def count(n):
    c=0
    if n<0:
        n=(n*-1)
    while n:
        r=n%10
        c+=1
        n=n//10
    return c
n,k=map(int,input().split())
l=list(map(int,input().split()))
r=[]
c=0
for i in l:
    if i<0:
        l=count(i)
        r.append(l)
    else:
        i=str(i)
        r.append(len(i))
c=0
for i in r:
    if i==k:
        c+=1
print(c)