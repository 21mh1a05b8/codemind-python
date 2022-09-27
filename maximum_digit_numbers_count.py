def count(n):
    if n<0:
        n=n*-1
    c=0
    while n:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    k=count(i)
    r.append(k)
m=max(r)
for i in l:
    if m==count(i):
        print(i,end=" ")