n=int(input())
p=list(map(int,input().split()))
c=[]
for i in range(0,n,2):
    j=1
    while j<=p[i+1]:
        c.append(p[i])
        j+=1
print(*c)