n=input()
m=input()
n=n.lower()
m=m.lower()
n=list(n)
m=list(m)
n=sorted(n)
m=sorted(m)
if n==m:
    print(True)
else:
    print(False)