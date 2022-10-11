n=int(input())
p=list(map(int,input().split()))
c,d=0,0
for i in range(2,n):
    if p[i-1]+p[i-2]==p[i]:
        c+=1
    else:
        d+=1
if c>0 and d==0:
    print("yes")
else:
    print("no")