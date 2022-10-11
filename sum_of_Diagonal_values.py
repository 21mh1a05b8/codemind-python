n,m=map(int,input().split())
b=[]
x=0
for i in range(n):
    a=list(map(int,input().split()))
    b.append(a)
s=0
for i in range(n):
    for j in range(m):
        if i==j or i+j==n-1:
            s+=b[i][j]
print(s)