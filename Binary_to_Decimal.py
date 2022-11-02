t=int(input())
for i in range(t):
    n=input()
    c=0
    k=n[::-1]
    for j in range(0,len(n)):
        if k[j]=="1":
            c+=2**j
    print(c)
        