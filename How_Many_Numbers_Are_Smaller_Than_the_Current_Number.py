n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    c=0
    for j in range(n):
        if l[i]>l[j]:
            c+=1
    print(c,end=" ")