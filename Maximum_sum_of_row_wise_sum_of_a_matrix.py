n,m=map(int,input().split())
r=[]
for i in range(n):
    a=list(map(int,input().split()))
    sum=0
    for j in a:
        sum=sum+j
    r.append(sum)
print(max(r))