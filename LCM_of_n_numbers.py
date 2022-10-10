def gcd(a,b):
    c=max(a,b)
    while True:
        if c%a==0 and c%b==0:
            return c
        c+=max(a,b)
n=int(input())
a=list(map(int,input().split()))
g=gcd(a[0],a[1])
for i in range(1,n):
    g=gcd(g,a[i])
print(g)