n=input().split()
p=n[-1]
k=min(p)
for i in k:
    h=k.lower()
    if k in p and h in p:
        print(h)
        break
else:
    print(k)