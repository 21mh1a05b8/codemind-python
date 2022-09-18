n=int(input())
m=int(input())
s1,s2=0,0
for i in range(1,n):
    if n%i==0:
        s1+=i
for i in range(1,m):
    if m%i==0:
        s2+=i
if s2==n and s1==m:
    print("Amicable")
else:
    print("Not Amicable")