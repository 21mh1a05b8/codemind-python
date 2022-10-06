n=int(input())
l=list(map(int,input().split()))
k=int(input())
r=[]
for i in range(k):
    last=l[n-1]
    for j in range(n-1,-1,-1):
        l[j]=l[j-1]
    l[0]=last
print(*l)