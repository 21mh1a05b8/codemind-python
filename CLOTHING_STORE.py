n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if l.count(i)>1:
        r.append(i)
s=set(r)
c=[]
for i in s:
    k=0
    if i in r:
        for j in r:
            if i==j:
                k+=1
    c.append(k)
sum=0
for i in c:
    sum=sum+(i//2)
print(sum)