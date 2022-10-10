n=int(input())
for i in range(1,n+1):
    k=ord("A")
    for j in range(i,n):
        print(" ",end="")
    for i in range(i):
        print(chr(k),end="")
        k+=1
    for j in range(i):
        print(chr(k-2),end="")
        k-=1
    k-=1
    print()
        