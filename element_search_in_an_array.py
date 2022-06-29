n=int(input())
l=list(map(int,input().split()))
k=int(input())
f=0
for i in l:
    if i==k:
        print(True)
        f+=1
        break
if f==0:
    print(False)