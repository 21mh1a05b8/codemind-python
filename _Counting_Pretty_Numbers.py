def last(x,y):
    c=0
    for i in range(x,y+1):
        r=i%10
        if r==2 or r==3 or r==9:
            c+=1
    print(c)
n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    last(a,b)