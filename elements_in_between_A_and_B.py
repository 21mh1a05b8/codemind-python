n=int(input())
a=list(map(int,input().split()))
A,B=map(int,input().split())
count=0
for i in a:
    if i>=A and i<=B:
        count+=1
        print(i,end=" ")
if count==0:
    print("-1")