n=int(input())
for i in range(1,n+1):
    k=1
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(k,end="")
        k+=1
    for j in range(1,i):
        print(k-2,end="")
        k-=1
    print()