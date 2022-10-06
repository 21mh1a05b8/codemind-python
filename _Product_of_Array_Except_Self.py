n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(n):
    pro=1
    for j in range(n):
        if i!=j:
            pro*=l[j]
    r.append(pro)            
print(*r)