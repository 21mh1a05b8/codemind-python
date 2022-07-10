n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if i%2==0:
        r.append(i)
if len(r)==len(l):
    print(True)
else:
    print(False)