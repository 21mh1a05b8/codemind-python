n=input()
n=list(set(n.lower()))
n=sorted(n)
for i in n:
    if i!=" " :
        print(i,end="")