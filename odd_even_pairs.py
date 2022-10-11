n=int(input())
k=list(map(int,input().split()))
c=[]
l=[]
for i in range(n):
    if k[i]%2!=0:
        c.append(k[i])
    else:
        l.append(k[i])
i,j=0,0
while i<len(c) or j<len(l):
    if i<len(c):
        print(c[i],end=" ")
        i+=1
    if j<len(l):
        print(l[j],end=" ")
        j+=1
if n%2!=0:
    print("0")