n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
s=0
for i in range(n):
    if l[i]==1:
        s+=(2**i)
print(s)