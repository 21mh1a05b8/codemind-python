n=int(input())
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    p=i-1
    for j in range(i-1):
        print(p,end="")
        p-=1
    for j in range(i):
        print(j,end="")
    print()