n=int(input())
a=list(map(int,input().split()))
add=0
for i in a:
    if i%2!=0:
        add+=1
if add<=2:
    print("YES")
else:
    print("NO")