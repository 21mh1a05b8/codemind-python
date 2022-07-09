n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
for i in l:
    if i%2==0:
        print(i)
        break