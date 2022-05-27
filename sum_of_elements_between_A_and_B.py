n=int(input())
a=list(map(int,input().split()))
A,B=map(int,input().split())
sum=0
for i in a:
    if i>=A and i<=B:
        sum=sum+i
print(sum)