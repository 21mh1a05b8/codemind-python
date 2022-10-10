n=int(input())
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(n,n+n):
        if i==0 or i==n-1 or j==n or j==n+n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()