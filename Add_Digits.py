def rem(n):
    count=0
    while n>0:
        r=n%10
        count+=1
        n=n//10
    return count
def sumnum(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    if rem(sum)==1:
        print(sum)
    else:
        sumnum(sum)
n=int(input())
sumnum(n)
    