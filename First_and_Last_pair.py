n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(n//2):
    print(l[i],end=" ")
    print(l[n-1-i],end=" ")
if n%2!=0:
    print(l[n//2],end=" 0")