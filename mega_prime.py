n=int(input())
for  i in range(2,(n//2)+1):
    if n%i==0:
        print("Not Mega Prime")
        break
else:
    c=0
    pd=0
    while n:
        r=n%10
        n=n//10
        c+=1
        if r==3 or r==5 or r==7:
            pd+=1
    if c==pd:
        print("Mega Prime")
    else:
        print("Not Mega Prime")