def count(n):
    c=0
    if n<0:
        n=(n*-1)
    while n:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i<0:
        print(count(i),end=" ")
    else:
        i=str(i)
        print(len(i),end=" ")