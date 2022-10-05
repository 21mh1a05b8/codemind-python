n=int(input())
l=list(map(int,input().split()))
c,m=0,0
for i in l:
    if i==1:
        c+=1
    else:
        c=0
    m=max(c,m)
print(m)