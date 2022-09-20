n=int(input())
if n<0:
    n=n*-1
    n=str(n)
    n=n[::-1]
    n=int(n)
    print(n*-1)
else:
    n=str(n)
    n=n[::-1]
    n=int(n)
    print(n)