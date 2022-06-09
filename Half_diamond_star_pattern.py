n=int(input())
k=1
if n>=3 and n<=100:
    for i in range(1,n*2):
        for j in range(1,k+1):
            print("*",end="")
        if i<n:
            k+=1
        else:
            k-=1
        print()
else:
    print("The pattern is not possible")