n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    k=l.count(i)
    if i not in r:
        r.append(i)
        print(i,end=" ")
        print(k,end=" ")