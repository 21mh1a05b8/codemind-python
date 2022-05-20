def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input())
for i in range(1,n+1):
    x=int(input())
    factorial=fact(x)
    print(factorial)