n=int(input())
l=list(map(int,input().split()))
a=l[n-1:(n//2)-1:-1]
print(*a,end=" ")
b=l[0:n//2:1]
print(*b)