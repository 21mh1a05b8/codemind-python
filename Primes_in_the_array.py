def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i>1:
        if prime(i):
            c+=1
print(c)