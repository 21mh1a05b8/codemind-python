n=int(input())
l=list(map(int,input().split()))
k=int(input())
sum=0
for i in l:
    if i>k:
        break
    else:
        sum=sum+i
print(sum)