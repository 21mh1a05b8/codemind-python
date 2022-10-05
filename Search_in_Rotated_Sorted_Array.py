n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(l)):
    if l[i]==k:
        c+=1
        print(i)
        break
if c==0:
    print("-1")