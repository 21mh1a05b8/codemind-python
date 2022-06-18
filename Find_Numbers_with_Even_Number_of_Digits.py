def l(n):
    le=0
    while(n>0):
        r=n%10
        le+=1
        n=n//10
    return le
n=int(input())
li=list(map(int,input().split()))
c=0
for i in li:
    x=l(i)
    if x%2==0:
        c+=1
print(c)