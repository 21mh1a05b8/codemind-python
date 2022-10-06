t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(k):
        last=l[n-1]
        for j in range(n-1,-1,-1):
            l[j]=l[j-1]
        l[0]=last
    print(*l)