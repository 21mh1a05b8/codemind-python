def self(n):
    c=0
    d=0
    t=n
    while n>0:
        r=n%10
        if r!=0 and t%r==0:
            c+=1
        n=n//10
        d+=1
    if d==c:
        print(t,end=" ")
x=int(input())
y=int(input())
for i in range(x,y+1):
    self(i)