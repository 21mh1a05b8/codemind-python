n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if i<0:
        i=i*-1
    r.append(len(str(i)))
m=max(r)
for i in l:
    if i<0:
        k=i*-1
    else:
        k=i
    if len(str(k))==m:
        print(i,end=" ")