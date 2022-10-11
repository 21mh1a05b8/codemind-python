n=int(input())
k=list(map(int,input().split()))
c,g=0,0
for i in range(1,n-1,2):
    if k[i-1]<k[i]:
        c+=1
    else:
        g+=1
if c>0 and g==0:
    print(c)
else:
    print("-1")