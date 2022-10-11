n=int(input())
k=list(map(int,input().split()))
c=0
if k[0]<k[1]:
    for i in range(1,n-1):
        if k[i-1]<k[i] and k[i+1]<k[i]:
            c+=1
        else:
            if k[i-1]>k[i] and k[i+1]>k[i]:
                c+=1
else:
    for i in range(1,n-1):
        if k[i-1]>k[i] and k[i+1]>k[i]:
            c+=1
        else:
            if k[i-1]<k[i] and k[i+1]<k[i]:
                c+=1
if c==n-2:
    print("yes")
else:
    print("no")