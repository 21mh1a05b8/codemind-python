n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
r=[]
sum=0
for i in l:
    if i>=a and i<=b:
        sum=sum+i
print(sum)