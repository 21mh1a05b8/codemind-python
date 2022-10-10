n=int(input())
p=0
i=0
while n:
    r=n%10
    p+=r*pow(8,i)
    n=n//10
    i+=1
l=1
k=0
while p:
    r=p%2
    k+=(r*l)
    l=l*10
    p=p//2
print(k)