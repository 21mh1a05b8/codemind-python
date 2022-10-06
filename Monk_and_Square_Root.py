t=int(input())
for i in range(t):
    x=-1
    a,b=map(int,input().split())
    for i in range(0,b):
        if (i*i)%b==a:
            x=i
            break
    print(x)    