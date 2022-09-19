n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i<0:
        i=i*-1
    i=str(i)
    print(len(i),end=" ")