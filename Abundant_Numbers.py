n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum>12:
    print(True)
else:
    print(False)