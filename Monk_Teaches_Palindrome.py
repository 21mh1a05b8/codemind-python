t=int(input())
for i in range(t):
    n=input()
    k=n[::-1]
    l=len(n)
    if k==n and l%2==0:
        print("YES EVEN")
    elif k==n and l%2!=0:
        print("YES ODD")
    else:
        print("NO")