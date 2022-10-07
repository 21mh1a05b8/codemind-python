n=int(input())
a=list(map(int,input().split()))
for i in range(n//2):
    print(a[i],end=" ")
    print(a[n-1-i],end=" ")
if n%2!=0:
    print(a[n//2],end=" ")
    print("0")