n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if l.count(i)==i:
        if i not in r:
            r.append(i)
sum=0
if len(r)==0:
    print("-1")
else:
    for i in r:
        sum=sum+i
    avg=sum/len(r)
    print("%.2f"%avg)