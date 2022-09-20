n=int(input())
l=list(map(int,input().split()))
if n%2!=0:
    for i in l:
        print(i,end=" ")
    print("0",end=" ")
else:
    for i in l:
        print(i,end=" ")