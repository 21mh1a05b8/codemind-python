def sum(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    return sum
n=int(input())
l=list(map(int,input().split()))
su=0
for i in l:
    s=sum(i)
    su=su+s
print(su)