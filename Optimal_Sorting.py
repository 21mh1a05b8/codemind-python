t=int(input())
for i in range(t):
    a=int(input())
    d=list(map(int,input().split()))
    if sorted(d)==d:
        print("0")
    else:
        print(max(d)-min(d))