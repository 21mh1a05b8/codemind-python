n=int(input())
k=n%10
n=n//10
l=n%10
n=n//10
p=n%10
n=n//10
d=n%10
n=n//10
if d==6:
    d=9
elif p==6:
    p=9
elif l==6:
    l=9
else:
    k=9
print(d,p,l,k,sep="")