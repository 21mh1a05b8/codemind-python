n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if i not in r:
        if i%2!=0:
            r.append(i)
print(len(r))