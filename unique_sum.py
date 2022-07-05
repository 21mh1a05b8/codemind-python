n=int(input())
l=list(map(int,input().split()))
r=[]
sum=0
for i in l:
    if i not in r:
        r.append(i)
for i in r:
    sum=sum+i
print(sum)