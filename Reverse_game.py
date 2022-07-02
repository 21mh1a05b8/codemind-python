def rev(n):
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
    return rev
n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    r.append(rev(i))
print(*r)