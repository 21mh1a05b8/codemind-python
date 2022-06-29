n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
        sum=sum+i
avg=sum//len(l)
f=0
for i in l:
    if i==avg:
        print(True)
        f+=1
        break
if f==0:
    print(False)